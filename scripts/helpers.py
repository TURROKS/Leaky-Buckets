#!/usr/bin python3
import requests
from scripts.constants import BASE_URI

__author__ = "Mario Rojas"
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Mario Rojas"
__status__ = "Dev"


def get_buckets_all(apikey, limit, offset):
    """ Returns all buckets found, accepts a limit argument """
    data = requests.get(BASE_URI + "s/{}/{}?access_token={}".format(offset, limit, apikey))
    print(data.json())


def get_buckets_with_keyword(apikey, keyword, limit, offset):
    """ Returns buckets based on the input keyword, accepts a limit argument """
    data = requests.get(BASE_URI+"s/{}/{}?access_token={}&keywords={}".format(offset, limit, apikey, keyword))
    print(data.json())


def get_bucket_by_id(apikey, bucket_id, limit, offset):
    """ Returns contents of a bucket based on its ID """
    data = requests.get(BASE_URI + "/{}/files/{}/{}?access_token={}".format(bucket_id, offset, limit, apikey))
    print(data.json())


def get_bucket_by_id_keyword(apikey, bucket_id, limit, offset, keyword):
    """ Returns contents of a bucket based on its ID """
    data = requests.get(BASE_URI + "/{}/files/{}/{}?access_token={}&keywords=".format(bucket_id, offset, limit, apikey,
                                                                                      keyword))
    print(data.json())
