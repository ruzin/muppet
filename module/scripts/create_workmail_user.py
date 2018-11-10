###Workmail Functions###

###Valid Exceptions for Workmail client###
#[MailDomainNotFoundException, OrganizationStateException, UnsupportedOperationException, 
#EntityAlreadyRegisteredException, MailDomainStateException, InvalidConfigurationException, OrganizationNotFoundException, 
#EntityStateException, EntityNotFoundException, ReservedNameException, InvalidParameterException, 
#DirectoryServiceAuthenticationFailedException, NameAvailabilityException, EmailAddressInUseException, 
#DirectoryUnavailableException, InvalidPasswordException]

#Create workmail user
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
    except workmail.exceptions.NameAvailabilityException as e:
        print "User already exists. Change the account_name and re-apply."
        sys.exit(1)
    except workmail.exceptions.InvalidPasswordException as e:
        print "Change your password. Password does not contain characters from at least 3 complexity categories."
        sys.exit(1)
    except ClientError as e:
        print(e.response['Error']['Code'])
        print(e.response['Error']['Message'])
        sys.exit(1)

#register workmail user
def register_workmail_user(org_id,user_id,email):
    try:
        response = workmail.register_to_work_mail(
            OrganizationId=org_id,
            EntityId=user_id,
            Email=email
        )
        print(response)
    except ClientError as e:
        print(e.response['Error']['Code'])
        print(e.response['Error']['Message'])
        sys.exit(1)
    


#Get workmail user email
def describe_workmail_user(org_id,user_id):
    try:
        response = workmail.describe_user(
        OrganizationId=org_id,
        UserId=user_id
        )
        print("Email-Id: "+response.get('Email'))
        return (response.get('Email'))
    except ClientError as e:
        print(e.response['Error']['Code'])
        print(e.response['Error']['Message'])
        sys.exit(1)

#Main method
if __name__ == "__main__":
    import os, sys, boto3
    from botocore.exceptions import ClientError

    #Set environment variables
    try:  
        os.environ["user_name"]
    except KeyError: 
        print "Please set the environment variable user_name"
        sys.exit(1)
    try:  
        os.environ["password"]
    except KeyError: 
        print "Please set the environment variable password"
        sys.exit(1)
    try:  
        os.environ["email"]
    except KeyError: 
        print "Please set the environment variable email"
        sys.exit(1)
    try:  
        os.environ["workmail_org_id"]
    except KeyError: 
        print "Please set the environment variable workmail_org_id"
        sys.exit(1)
    
    #Set env variables as locals
    user_name=os.environ['user_name']
    password=os.environ['password']
    email=os.environ['email']
    workmail_org_id=os.environ['workmail_org_id']

    #Set boto3 session
    session = boto3.Session(profile_name='sandbox')

    #select workmail service
    workmail = session.client('workmail')

    #Call functions
    user_id = create_workmail_user(workmail_org_id,user_name,user_name,password)
    register_workmail_user(workmail_org_id,user_id,email)
    describe_workmail_user(workmail_org_id,user_id)




    
    
