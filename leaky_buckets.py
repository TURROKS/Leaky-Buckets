#!/usr/bin python3

import argparse
import scripts.helpers as funcs

__author__ = "Mario Rojas"
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Mario Rojas"
__status__ = "Dev"


parser = argparse.ArgumentParser(description="This Tool leverages Gray Hat Warfare to look for exposed storage buckets",
                                 epilog='Enjoy the tool')
parser.add_argument('-a', '--api', type=str, required=True)
parser.add_argument('-b', '--bucket', type=int, help="Bucket ID")
parser.add_argument('-k', '--keyword', type=str, help="Keyword to search")
parser.add_argument('-l', '--limit', default=100, help="Limit results")
parser.add_argument('-s', '--start', default=0, type=int, help="Buckets Offset")

# Global Arguments
args = parser.parse_args()


def main():

    """ Confirm API """
    if args.api:
        """ Select Function """
        if args.keyword:
            funcs.get_buckets_with_keyword(args.api, args.keyword, args.limit, args.start)
        elif args.bucket:
            funcs.get_bucket_by_id(args.api, args.bucket, args.limit, args.start)
        else:
            funcs.get_buckets_all(args.api, args.limit, args.start)


if __name__ == '__main__':
    main()
