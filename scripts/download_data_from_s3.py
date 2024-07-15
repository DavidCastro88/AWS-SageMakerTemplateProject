import boto3
import os
"""
Function to download an individual file from S3.
"""
def download_file_from_s3(bucket_name, s3_key, local_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_key, local_path)
        print(f'Successfully downloaded s3://{bucket_name}/{s3_key} to {local_path}')
    except Exception as e:
        print(f'Error downloading file from S3: {e}')
        
"""
Function to download all files from a specific prefix in S3 to a local directory,
maintaining the directory structure.
"""
def download_directory_from_s3(bucket_name, s3_prefix, local_directory):
    # Initialize the S3 client
    s3 = boto3.client('s3')
    
    # Create a paginator to handle the listing of objects in S3 bucket
    paginator = s3.get_paginator('list_objects_v2')
    
    # Paginate through the objects in the specified bucket and prefix
    pages = paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix)

    # Iterate through each page of listed objects
    for page in pages:
        # Check if the page contains any objects
        if 'Contents' in page:
            # Iterate through each object in the page
            for obj in page['Contents']:
                # Get the S3 key (path) of the object
                s3_key = obj['Key']
                
                # Create the local path where the object will be downloaded
                local_path = os.path.join(local_directory, os.path.relpath(s3_key, s3_prefix))
                
                # Get the directory path of the local file
                local_dir = os.path.dirname(local_path)

                # If the directory does not exist, create it
                if not os.path.exists(local_dir):
                    os.makedirs(local_dir)
                download_file_from_s3(bucket_name, s3_key, local_path)

if __name__ == '__main__':
    bucket_name = 'your-bucket-name'
    s3_prefix = 'ruta/de/s3'
    local_directory = '../data/raw'
    download_directory_from_s3(bucket_name, s3_prefix, local_directory)