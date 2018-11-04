###python script to create workmail user and output email address###


import boto3, os

#select workmail service
workmail = boto3.client('workmail')

#create user
def create_workmail_user(org_id,name,display_name,passwd):
    response = workmail.create_user(
        OrganizationId=org_id,
        Name=name,
        DisplayName=display_name,
        Password=passwd
    )
    print(response)

#describe user that was just created
def describe_workmail_user(org_id,user_id):
    response = workmail.describe_user(
        OrganizationId=org_id,
        UserId=user_id
    )
    print(response)