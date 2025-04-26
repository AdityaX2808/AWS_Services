import boto3

s3 = boto3.client('s3')
bucket_name = 'moibucket48'
file_path = r"D:\projects\BL_DE_Digit Insurance\PostgressSQL\data\country_wise_latest.csv"
object_path = 'country_wise.csv'

s3.upload_file(file_path, bucket_name, object_path)
print("File uploaded Successfully !!..")

