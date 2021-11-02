#
#  Copyright 2020-2021 Viens Consulting, LLC. All Rights Reserved.
#

import boto3
import util

# AWS Security Token Service API convienence class
# https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html


class STS:

    # Constructor: create an STS client
    def __init__(self):
        self.sts_client = boto3.client('sts')

    # Retreive aws user identity info
    def get_aws_identity(self):
        return self.sts_client.get_caller_identity()


# TEST DRIVER

sts = STS()
aws_identity = sts.get_aws_identity()

payload = {
    'aws_account': aws_identity
}

util.prettyprint(payload)
