#!/bin/bash

# Create AWS CodePipeline Service Role
#
aws iam create-role \
--description "My service-linked role to support CodePipeline" \
--aws-service-name lex.amazonaws.com

aws iam create-role \
--role-name DeepakDeveloperToolsServiceRole \
--assume-role-policy-document file://trust-policy.json

# Create S3 bucket where build artifacts will be saved. Because bucket
# names must be globally unique, I typically use the following naming
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



# Create CodeBuild Project
# Source: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html
create-project
--name <value>
[--description <value>]
--source <value>
[--secondary-sources <value>]
[--source-version <value>]
[--secondary-source-versions <value>]
--artifacts <value>
[--secondary-artifacts <value>]
[--cache <value>]
--environment <value>
--service-role <value>
[--timeout-in-minutes <value>]
[--queued-timeout-in-minutes <value>]
[--encryption-key <value>]
[--tags <value>]
[--vpc-config <value>]
[--badge-enabled | --no-badge-enabled]
[--logs-config <value>]
[--file-system-locations <value>]
[--build-batch-config <value>]
[--concurrent-build-limit <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]

aws codebuild create-project --generate-cli-skeleton


# Create CodeDeploy
# Source: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html

# Create CodePipeline
# Source: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html


