#!/usr/bin/env python3
"""func task 15"""
from pymongo import MongoClient


def func_nginx(nginx_collection):
    """Prints stats Nginx request logs"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for meth in methods:
        req_cx = len(list(nginx_collection.find({'method': meth})))
        print('\tmethod {}: {}'.format(meth, req_cx))

    status_count = len(list(nginx_collection.find({'method': 'GET',
                                                   'path': '/status'})))
    print('{} status check'.format(status_count))


def print_top(server_collection):
    """Prints statistics about the top 10 HTTP IPs in a collection."""
    print('IPs:')

    requestxs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )

    for reqx in requestxs:
        ip = reqx['_id']
        ip_reqsc = reqx['totalRequests']

        print('\t{}: {}'.format(ip, ip_reqsc))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')

    func_nginx(client.logs.nginx)
    print_top(client.logs.nginx)


if __name__ == '__main__':
    run()
