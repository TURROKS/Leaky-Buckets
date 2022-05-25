#!/usr/bin python3
from datetime import datetime as dt
import requests
from colorama import init
from termcolor import colored
from scripts.constants import BASE_URI
from scripts.constants import LOGO

__author__ = "Mario Rojas"
__license__ = "MIT"
__version__ = "0.2.0"
__maintainer__ = "Mario Rojas"
__status__ = "Dev"

# Instantiate colorama
init()


def get_buckets_all(apikey, limit, offset):
    """ Returns all buckets found, accepts a limit argument """
    data = requests.get(BASE_URI + "s/{}/{}?access_token={}".format(offset, limit, apikey))
    parsed = data.json()
    if parsed['buckets_count'] > 0:
        print(colored(LOGO, 'red') + '\n')
        print('\n'+"{:<7} {:<70} {:<10} {:<10} {:<10}".format('ID', 'Bucket', 'File Count', 'Type', 'Container'))
        for bucket in parsed['buckets']:

            bucket_id = bucket['id']
            bucket_name = bucket['bucket']
            file_count = bucket['fileCount']
            bucket_type = bucket['type']
            try:
                container = bucket['container']
            except KeyError:
                container = ''
            print("{:<7} {:<70} {:<10} {:<10} {:<10}".format(bucket_id, bucket_name, file_count, bucket_type,
                                                             container))
        print('\n'+colored(parsed['notice'], 'green'),)
    else:
        print("No Buckets Found")


def get_buckets_with_keyword(apikey, keyword, limit, offset):
    """ Returns buckets based on the input keyword, accepts a limit argument """
    data = requests.get(BASE_URI+"s/{}/{}?access_token={}&keywords={}".format(offset, limit, apikey, keyword))
    parsed = data.json()
    if parsed['buckets_count'] > 0:
        print(colored(LOGO, 'red') + '\n')
        print('\n'+"{:<7} {:<70} {:<10} {:<10} {:<10}".format('ID', 'Bucket', 'File Count', 'Type', 'Container'))
        for bucket in parsed['buckets']:

            bucket_id = bucket['id']
            bucket_name = bucket['bucket']
            file_count = bucket['fileCount']
            bucket_type = bucket['type']
            try:
                container = bucket['container']
            except KeyError:
                container = ''
            print("{:<7} {:<70} {:<10} {:<10} {:<10}".format(bucket_id, bucket_name, file_count, bucket_type, container))
        print('\n'+colored(parsed['notice'], 'green'))
    else:
        print("No Buckets Found")


def get_bucket_by_id(apikey, bucket_id, limit, offset):
    """ Returns contents of a bucket based on its ID """
    data = requests.get(BASE_URI + "/{}/files/{}/{}?access_token={}".format(bucket_id, offset, limit, apikey))
    parsed = data.json()
    print(colored(LOGO, 'red') + '\n')
    print('\n' + "{:<7} {:<45} {:<10} {:<20}".format('ID', 'Filename', 'Size', 'Modified'))
    for file in parsed['files']:

        file_id = file['id']
        filename = file['filename']
        size = file['size']
        modified = dt.fromtimestamp(file['lastModified']).strftime('%Y-%m-%d %H:%M:%S')

        # Keys available for future use
        # bucket = file['bucket']
        # bucket_id = file['bucketId']
        # path = file['fullPath']
        # url = file['url']
        # type = file['type']

        print("{:<7} {:<45} {:<10} {:<20}".format(file_id, filename, size, modified))
    print('\n' + colored(parsed['notice'], 'green'))


def get_bucket_by_id_keyword(apikey, bucket_id, limit, offset, keyword):
    """ Returns contents of a bucket based on its ID """
    data = requests.get(BASE_URI + "/{}/files/{}/{}?access_token={}&keywords=".format(bucket_id, offset, limit, apikey,
                                                                                      keyword))
    parsed = data.json()
    print(colored(LOGO, 'red') + '\n')
    print('\n' + "{:<7} {:<45} {:<10} {:<20}".format('ID', 'Filename', 'Size', 'Modified'))
    for file in parsed['files']:

        file_id = file['id']
        filename = file['filename']
        size = file['size']
        modified = dt.fromtimestamp(file['lastModified']).strftime('%Y-%m-%d %H:%M:%S')

        # Keys available for future use
        # bucket = file['bucket']
        # bucket_id = file['bucketId']
        # path = file['fullPath']
        # url = file['url']
        # type = file['type']

        print("{:<7} {:<45} {:<10} {:<20}".format(file_id, filename, size, modified))
    print('\n' + colored(parsed['notice'], 'green'))
