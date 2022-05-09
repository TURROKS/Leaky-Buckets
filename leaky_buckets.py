#!/usr/bin python3

import argparse
import scripts.helpers as funcs

__author__ = "Mario Rojas"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Mario Rojas"
__status__ = "Dev"


parser = argparse.ArgumentParser(description="This Tool leverages Gray Hat Warfare to look for exposed storage buckets",
                                 epilog='Enjoy the tool')
parser.add_argument('-a', '--api', type=str, default='', help='Enter your API Key')
parser.add_argument('-k', '--keyword', default="mp3", help="Keyword to search")
parser.add_argument('-l', '--limit', default=100, help="Limit results")

# Global Arguments
args = parser.parse_args()


def main():

    if args.api:
        funcs.get_buckets(args.api, args.keyword, args.limit)


if __name__ == '__main__':
    main()
