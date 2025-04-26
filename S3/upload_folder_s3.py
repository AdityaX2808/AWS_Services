import os
import boto3

s3 = boto3.client('s3')

bucket_name = 'moibucket48'
local_folder = r"D:\projects\BL_DE_Digit Insurance\PostgressSQL\data"
s3_folder = '' 

file_counter = 0

for root, dirs, files in os.walk(local_folder):
    for file in files:
        if file.endswith(".csv"):  
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_folder)
            s3_key = os.path.join(s3_folder, relative_path).replace("\\", "/")

            try:
                s3.upload_file(local_path, bucket_name, s3_key)
                print(f" Uploaded: {s3_key}")
                file_counter += 1
            except Exception as e:
                print(f" Failed to upload {s3_key}: {e}")

print(f"\n Total files uploaded: {file_counter}")
