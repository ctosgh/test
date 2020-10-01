import boto3

s3 = boto3.resource('s3')

location = {'LocationConstraint': 'us-west-2'}

for bucket in s3.buckets.all():
    print("find existing bucket {}".format(bucket.name))
    for key in bucket.objects.all():
        print("key is {}".format(key.key))
    print("will delete bucket {}".format(bucket.name))
    bucket.delete()

print("now creating bucket jsunbucket")
s3.create_bucket(Bucket="jsunbucket", CreateBucketConfiguration=location)
