import boto3

ec2_instance = boto3.resource('ec2' , region_name = 'ap-south-1')

instance = ec2_instance.create_instances(
    ImageId = 'ami-002f6e91abff6eb96' , 
    InstanceType = 't2.micro' , 
    MinCount = 1 , 
    MaxCount = 1 ,
    KeyName = 'Aditya' , 
    SecurityGroupIds = ['sg-0058d56bde5fd86db'] ,
)

print("Instance Created:" , instance[0].id)