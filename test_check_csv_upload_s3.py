import pytest
import boto3


def check_csv_uploaded_to_s3(bucket_name, csv_file):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    uploaded_files = [obj['Key'] for obj in response.get('Contents', [])]
    return csv_file in uploaded_files


@pytest.mark.parametrize("bucket_name, csv_file", [("test-bucket", "file1.csv")])
def test_check_csv_uploaded_to_s3(bucket_name, csv_file, mocker):
    mock_s3_client = mocker.patch.object(boto3, 'client')
    mock_s3_client.return_value.list_objects_v2.return_value = {'Contents': [{'Key': 'file1.csv'}]}

    assert check_csv_uploaded_to_s3(bucket_name, csv_file)
