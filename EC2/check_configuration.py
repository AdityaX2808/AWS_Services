import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_ec2_instances():
    try:
        # Create an EC2 client
        ec2 = boto3.client('ec2')
        
        # Describe instances
        response = ec2.describe_instances()
        
        # Check if instances are available
        reservations = response.get('Reservations', [])
        
        if not reservations:
            print("No EC2 instances found in your AWS account.")
        else:
            print(f"Found {len(reservations)} EC2 instance(s):")
            
            # Loop through the reservations to print details of instances
            for reservation in reservations:
                for instance in reservation.get('Instances', []):
                    instance_id = instance.get('InstanceId')
                    instance_type = instance.get('InstanceType')
                    state = instance.get('State', {}).get('Name')
                    public_ip = instance.get('PublicIpAddress', 'No Public IP')
                    private_ip = instance.get('PrivateIpAddress', 'No Private IP')
                    launch_time = instance.get('LaunchTime')

                    print(f"\nInstance ID: {instance_id}")
                    print(f"Instance Type: {instance_type}")
                    print(f"State: {state}")
                    print(f"Public IP: {public_ip}")
                    print(f"Private IP: {private_ip}")
                    print(f"Launch Time: {launch_time}")

    except NoCredentialsError:
        print("Error: AWS credentials are missing or not configured correctly.")
    
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found. Please check the credentials file.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")


list_ec2_instances()

