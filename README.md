# Homework Assignment 2

## Assignment

Implement a photo album web application that can be searched using natural language through both text and voice. You will learn how to use Lex, ElasticSearch, and Rekognition to create an intelligent search layer to query your photos for people, objects, actions, landmarks and more.

## Outline

This assignment has eight components:

1. Launch an OpenSearch Instance
2. Upload & Index Photos
3. Search
4. Build the API Layer
5. Frontend
6. Implement Voice accessibility in the frontend
7. Deploy your code using CodePipeline
8. Create AWS CloudFormation template for the stack


## 1. Launch an ElasticSearch instance

- Using AWS ElasticSearch service2, create a new domain called “photos”. 
- Make note of the Security Group (SG1) you attach to the domain.
- Deploy the service inside a VPC3.  
-- This prevents unauthorized internet access to your service.

## 2. Upload & Index Photos

abc

## 3. Search

abc

## 4. Build the API Layer

abc

## 5. Frontend

abc

## 6. Implement Voice accessibility in the frontend

abc

## 7. Deploy your code using CodePipeline

abc

## 8. Create AWS CloudFormation template for the stack

abc
### Resources to create

1. Default VPC
2. Default Subnets (a, b, c)
3. Default Security Group
4. S3 Bucket 1 (S3-1) - Photos
5. S3 Bucket 2 (S3-2)
6. Open Search Domain (OS-1)
7. Lambda Function 1 (LF-1)
8. Lambda Function 2 (LF-2)
9. CodePipeline 1 (PL-1)
10. CodePipeline 2 (PL-2)

Upload Photo Sequence of Events
1. Upload Photo to S3-1
   1. Trigger LF-1 passing S3 key to photo in S3-1 + additional user supplied labels passed as metadata
   2. LF-1 submits photo to AWS Rekognition returning labels
   3. LF-1 adds user supplied labels + rekognition labels + photo S3 key to open search index
