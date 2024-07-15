import boto3
import os

"""
Function to individual file to S3, 
maintaining the directory structure.
"""
def upload_file_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f'Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}')
    except Exception as e:
        print(f'Error uploading file to S3: {e}')

"""
Function to upload all files in a directory to S3, 
maintaining the directory structure.
"""
def upload_directory_to_s3(directory_path, bucket_name):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, directory_path)
            upload_file_to_s3(file_path, bucket_name, s3_key)

if __name__ == '__main__':
    bucket_name = 'your-bucket-name'
    directory_path = '../data/raw'
    upload_directory_to_s3(directory_path, bucket_name)