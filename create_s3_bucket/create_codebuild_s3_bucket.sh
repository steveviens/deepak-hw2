#!/bin/bash

# Create S3 bucket where build artifacts will be saved. AWS bucket
# names must be globally unique. I typically use the following naming
# convension when creating S3 buckets:
#
#     {bucket-name}.{region-name}.{account-id}
#
#   Examples:
#
#     repo.us-east-1.1234567890
#     codebuild.us-east-1.1234567890
#
aws s3 mb s3://repo.us-east-1.677126791323
