import boto3, os

#select workmail service
workmail = boto3.client('workmail')

#create user
def create_workmail_user(org_id,name,display_name,passwd):
response = client.create_user(
    OrganizationId=org_id,
    Name=name,
    DisplayName=display_name,
    Password=passwd
)

