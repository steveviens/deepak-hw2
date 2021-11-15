#!/bin/bash

# Create CodePipeline Service Role
aws iam create-role \
--description "My CodePipeline Service Role" \
--role-name DeepakCodePipelineServiceRole \
--assume-role-policy-document file://codebuild_trustpolicy.json

# Attach Iam Policy to your CodePipeline Service Role
aws iam put-role-policy \
--role-name DeepakCodePipelineServiceRole \
--policy-name DeepakCodePipelinePolicy \
--policy-document file://policy.json

# View your new Service Role
aws iam get-role \
--role-name DeepakCodePipelineServiceRole

# View permission policy attached to new Service Role
aws iam get-role-policy \
--role-name DeepakCodePipelineServiceRole \
--policy-name DeepakCodePipelinePolicy
