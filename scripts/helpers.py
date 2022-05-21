#!/usr/bin python3
import requests
from scripts.constants import BASE_URI

__author__ = "Mario Rojas"
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Mario Rojas"
__status__ = "Dev"


def get_buckets_all(apikey, limit, start):
    """ Returns all buckets found, accepts a limit argument """
    data = requests.get(BASE_URI + "{}/{}?access_token={}".format(start, limit, apikey))
    print(data.json())


def get_buckets_with_keyword(apikey, keyword, limit):
    """ Returns buckets based on the input keyword, accepts a limit argument """
    data = requests.get(BASE_URI+"0/{}?access_token={}&keywords={}".format(limit, apikey, keyword))
    print(data.json())
