# ETL_learning_using_aws-
Using AWS service to do an ETL process from MySQL to S3 

# How?

1) MySQL is connected to an AWS RDS. (with the required security group allowed in all IPv4, IPv6 and DB of choice allowed in all)
2) AWS DMS with RDS and S3 endpoints. (need 2 forms and a target S3 bucket in advance)
3)The lambda function must be set to trigger on the S3 bucket of your choice.
4) Use Boto3 to trigger a glue job in the lambda function.
5) As the glue job is triggered, you can get the updated file from the S3 target bucket.

# Note
You need to perform a load operation (select in MySQL) to trigger the DMR and load it to S3.
Then the next upcoming changes or queries will be executed, but without the data in S3, we will not be able to perform the operation.
DMR needs to be restored every time it is stopped. (no resume).
