#!/usr/bin python3
import requests
from scripts.constants import BASE_URI

__author__ = "Mario Rojas"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Mario Rojas"
__status__ = "Dev"


def get_buckets(apikey, keyword, limit):

    data = requests.get(BASE_URI+"0/{}?access_token={}&keywords={}".format(limit, apikey, keyword))
    print(data.json())
