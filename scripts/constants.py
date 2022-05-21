from typing import NamedTuple

__author__ = "Mario Rojas"
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Mario Rojas"
__status__ = "Dev"

BASE_URI = "https://buckets.grayhatwarfare.com/api/v1/bucket"


class BucketFile(NamedTuple):
    id: int
    bucket: str
    bucketId: int
    filename: str
    fullPath: str
    url: str
    size: int
    type: str
    lastModified: str
