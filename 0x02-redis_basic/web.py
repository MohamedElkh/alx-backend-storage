#!/usr/bin/env python3
"""func Implementing an expiring web cache and tracker"""
import requests
import redis

rr = redis.Redis()
num = 0


def get_page(url: str) -> str:
    """func to track how many times a particular URL"""
    rr.set(f"cached:{url}", num)
    res = requests.get(url)

    rr.incr(f"count:{url}")
    rr.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))

    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
