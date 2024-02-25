import pytest
import boto3


def check_s3_connection(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    return bucket in s3.buckets.all()


@pytest.mark.parametrize("bucket_name", ["test-bucket"])
def test_check_s3_connection(bucket_name, mocker):
    mock_s3_resource = mocker.patch.object(boto3, 'resource')
    mock_bucket = mock_s3_resource.return_value.Bucket.return_value
    mock_bucket in mock_s3_resource.return_value.buckets.all.return_value = True

    assert check_s3_connection(bucket_name)
