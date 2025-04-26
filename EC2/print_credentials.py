import os

def print_aws_files():
    aws_credentials_path = os.path.expanduser("~/.aws/credentials")
    aws_config_path = os.path.expanduser("~/.aws/config")

    if os.path.exists(aws_credentials_path):
        print(f"Contents of {aws_credentials_path} (AWS Credentials):")
        with open(aws_credentials_path, 'r') as file:
            print(file.read())  
    else:
        print(f"Error: The credentials file does not exist at {aws_credentials_path}")

    if os.path.exists(aws_config_path):
        print(f"\nContents of {aws_config_path} (AWS Config):")
        with open(aws_config_path, 'r') as file:
            print(file.read())  
    else:
        print(f"Error: The config file does not exist at {aws_config_path}")


print_aws_files()
