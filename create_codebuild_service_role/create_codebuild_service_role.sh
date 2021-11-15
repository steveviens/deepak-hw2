#!/bin/bash

# Create CodeBuild service role
aws iam create-role \
--description "My CodeBuild Service Role" \
--role-name DeepakCodeBuildServiceRole \
--assume-role-policy-document file://codebuild_trustpolicy.json

# Attach IAM policy to your CodeBuild service role
aws iam put-role-policy \
--role-name DeepakCodeBuildServiceRole \
--policy-name DeepakCodeBuildPolicy \
--policy-document file://codebuild_policy.json

# View CodeBuild service role
aws iam get-role \
--role-name DeepakCodeBuildServiceRole

# View permission policy attached to new service role
aws iam get-role-policy \
--role-name DeepakCodeBuildServiceRole \
--policy-name DeepakCodeBuildPolicy
