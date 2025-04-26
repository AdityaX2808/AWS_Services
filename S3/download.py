import boto3

# Initialize session and S3 client
session = boto3.session.Session(profile_name="default", region_name="ap-south-1")
s3 = session.client("s3")

# Download file
bucket_name = "moibucket48"
s3_key = "worldometer_data.csv"
local_download_path = "C:/Users/Aditya/world.csv"

try:
    s3.download_file(bucket_name, s3_key, local_download_path)
    print(f" File downloaded to: {local_download_path}")
except Exception as e:
    print(f" Download failed: {e}")