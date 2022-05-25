# Leaky-Buckets
Search for exposed cloud storage buckets, currently using [GrayHatWarfare](https://grayhatwarfare.com/)

### Usage

#### All Buckets
`leaky_buckets.py -a <YOUR_KEY> -l <Results Limit>`

![Example1](https://github.com/TURROKS/Leaky-Buckets/blob/master/misc/image1.png)

#### Buckets by keyword
`leaky_buckets.py -a <YOUR_KEY> -k <Keyword> -l <Results Limit>`

![Example2](https://github.com/TURROKS/Leaky-Buckets/blob/master/misc/image2.png)

#### Buckets by ID
`leaky_buckets.py -a <YOUR_KEY> -b <Bucket ID> -l <Results Limit>`
#### Buckets by ID and Keyword
`leaky_buckets.py -a <YOUR_KEY> -b <Bucket ID> -k <Keyword> -l <Results Limit>`

### Arguments

| Flags         | Description                |
|---------------|----------------------------|
| -h,  --help   | show help message and exit |
| -a, --api     | Enter your API             |
| -b, --bucket  | The ID of a Bucket         |
| -k, --keyword | Keyword for search         |
| -l, --limit   | Results Limit              |
| -s, --start   | Offset for the results     |

### Disclaimer:

Usage of Leaky-Buckets for accessing the buckets without prior mutual consistency can be considered as an illegal 
activity. 

It is the final user's responsibility to obey all applicable local, state and federal laws. 

**Authors assume no liability and are not responsible for any misuse or damage caused by this program.**
