#!/usr/bin/env python3
"""Reading from Redis and recovering original type Incrementing values"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any, Optional


def call_history(method: Callable) -> Callable:
    """func to store the history of inputs"""
    key = method.__qualname__

    outps = key + ":outputs"
    inps = key + ":inputs"

    @wraps(method)
    def func_wrap(self, *args, **kwds):
        """func to store the wrapper"""
        self._redis.rpush(inps, str(args))

        data = method(self, *args, **kwds)
        self._redis.rpush(outps, str(data))

        return data
    return func_wrap


def count_calls(method: Callable) -> Callable:
    """func to count many times methods of the Cache class"""
    key = method.__qualname__

    @wraps(method)
    def func_wrapper(self, *args, **kwds):
        """func to the wrapped function """
        self._redis.incr(key)

        return method(self, *args, **kwds)
    return func_wrapper


class Cache:
    """the class to implement"""
    def __init__(self):
        """func constructor store an instance of the Redis client"""
        self._redis = redis.Redis()

        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key, store the input data"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """take a key string argument and an optional Callable argument"""
        data = self._redis.get(key)

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """ func automatically parametrize Cache.get to str """
        data = self._redis.get(key)

        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ automatically parametrize Cache.get to int """
        data = self._redis.get(key)

        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0

        return data

    def replay(method: Callable):
        """ display the history of calls of a particular function """
        key = method.__qualname__

        inp = key + ":inputs"
        outp = key + ":outputs"

        redisx = method.__self__._redis
        countt = redisx.get(key).decode("utf-8")
        print("{} was called {} times:".format(key, countt))

        inputlistx = redisx.lrange(inp, 0, -1)
        outputlistx = redisx.lrange(outp, 0, -1)

        zippedx = list(zip(inputlistx, outputlistx))

        for aa, bb in zippedx:
            attr, data = aa.decode("utf-8"), bb.decode("utf-8")

            print("{}(*{}) -> {}".format(key, attr, data))
