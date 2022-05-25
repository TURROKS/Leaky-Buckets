# Leaky-Buckets

A big concern for organizations of all sizes is knowing what information they are exposing to the world, the perimeter we used to know has dramatically changed with the improvements and reduction on the costs associated with cloud storage, more companies are relying on this services to get their apps and services up and running.

This has created a huge problem for security teams which now need to be aware of all the new "Buckets" that are created by developers and system admins to contain the files required for these apps to work.

The idea behind "Leaky-Buckets" is to simplify the duties of these security teams, by allowing them to search for exposed cloud storage buckets, this tool is currently using [GrayHatWarfare](https://grayhatwarfare.com/)

### Usage

You can use this tool to search for Buckets and Files based on keywords i.e. (Company Name, Company Domain, Application Name, etc.)

#### All Buckets
Returns a list of all the buckets available

`leaky_buckets.py -a <YOUR_KEY> -l <Results Limit>`

![Example1](https://github.com/TURROKS/Leaky-Buckets/blob/main/misc/image1.png)

#### Buckets by keyword
Returns only the buckets that match the desired keyword

`leaky_buckets.py -a <YOUR_KEY> -k <Keyword> -l <Results Limit>`

![Example2](https://github.com/TURROKS/Leaky-Buckets/blob/main/misc/image2.png)

#### Bucket details by ID
Returns details about the files contain inside a bucket

`leaky_buckets.py -a <YOUR_KEY> -b <Bucket ID> -l <Results Limit>`
#### Buckets by ID and Keyword
Returns details about the files based on a keyword contain inside a bucket

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
