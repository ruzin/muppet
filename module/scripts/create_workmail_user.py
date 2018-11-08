#Functions
#create user
def create_workmail_user(org_id,name,display_name,password):
    try:
        response = workmail.create_user(
            OrganizationId=org_id,
            Name=name,
            DisplayName=display_name,
            Password=password
        )
        print(response)
        return (response.get('UserId'))
    except workmail.exceptions.NameAvailabilityException:
        print "User already exists"


#register user
def register_workmail_user(org_id,user_id,email):
    try:
        response = workmail.register_to_work_mail(
            OrganizationId=org_id,
            EntityId=user_id,
            Email=email
        )
        print(response)


#get user email
def describe_workmail_user(org_id,user_id):
    response = workmail.describe_user(
        OrganizationId=org_id,
        UserId=user_id
    )
    print(response)
    return (response.get('Email'))
        


#Main method
if __name__ == "__main__":
    import os, sys, boto3
    from botocore.exceptions import ClientError, ParamValidationError

    session = boto3.Session(profile_name='sandbox')

    #select workmail service
    workmail = session.client('workmail')
    iam = session.client('iam')

    #set environment variables
    user_name=os.environ['user_name']
    password=os.environ['password']
    workmail_org_id=os.environ['workmail_org_id']


    user_id = create_workmail_user(workmail_org_id,user_name,user_name,password)
    #register_workmail_user(workmail_org_id,user_id,email)
    #email = describe_workmail_user(workmail_org_id,user_id)
    #print(email)




    
    
