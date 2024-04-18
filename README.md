# serverless-example
Serverless framework, Docker and Localstack example with Python, Using S3, DynamoDB, API Gateway.

## Run Test

Install Local src so that we can import in UnitTest easily
    
    pip install -e src

Run Tests

    pytest

### Running the API Gateway

    http://localhost:4566/restapis/9bbj2ox5px/local/_user_request_/images/all

## AWS Commands

API Gateway

    awslocal apigateway get-resources --rest-api-id 9bbj2ox5px

S3 List buckets

    awslocal s3api list-buckets

S3 CP File

    awslocal s3 cp /opt/image/voters_short.png s3://mario-thumbnails/

S3 list objects

    awslocal s3 ls s3://mario-thumbnails/

DynamoDB list tables
    
    awslocal dynamodb list-tables

DynamoDB scan items

    awslocal dynamodb scan --table img-url-table
