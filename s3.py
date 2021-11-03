#
#  Copyright 2020-2021 Viens Consulting, LLC. All Rights Reserved.
#

import boto3
import util


class S3:

    # Constructor: create an STS client
    def __init__(self):
        self.s3_client = boto3.resource('s3')

    # Create an S3 bucket
    def put_object(self):
        return {}


# Example
s3 = S3()
results = s3.put_object()
util.prettyprint(results)
