# Muppet
## Description
Muppet is a combination of python/terraform scripts that fully automates and version controls AWS account creation. 

Use Case
-------------------------------
Organizations/Individuals that have an existing AWS master/billing account and want to create multiple AWS accounts with billing tied to their master account. Muppet is not suitable if your use case is to create a personal/singular AWS account.

Core Components
-------------------------------
The core components of muppet are:

- **[AWS Workmail](https://aws.amazon.com/workmail/)**: Muppet uses the workmail API to automate the create of email accounts, a requirement when creating an AWS account.
- **[Terraform](https://www.terraform.io/)**: Muppet uses Terraform to create the AWS account in AWS Organizations and store the config state. In the near future, the goal is to configure workmail via terraform as well.
- **[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)**: Muppet used Boto3, the AWS python SDK, to create email accounts in AWS workmail.

Pre-requisites
-------------------------------
Prior to using Muppet, the following pre-requisites need to be in place:

- **[AWS Organizations](https://aws.amazon.com/organizations/)**: Set up AWS Organizations in your master/billing AWS account. All accounts that you create using Muppet will fall under this Organization.
- **[AWS Workmail](https://aws.amazon.com/workmail/)**: Create an AWS workmail account. The first 25 users are free to create and then its $4 per user per month.
- **Terraform/Boto3**: Ensure that you have installed Terraform/Boto3 in the environment that you are running Muppet in. Familiarize yourself with the concept of [Modules](https://www.terraform.io/docs/modules/usage.html) in Terraform.
- **Configure AWS Credentials**: Configure your AWS credentials with read/write access to AWS Workmail and AWS Organizations in your AWS account.

Getting Started & Documentation
-------------------------------
Muppet is very simple to use, hence the name :P. To get started:
- Clone the repository
```
$ git clone git@github.com:ruzin/muppet.git
```
- In example.tf, provide your custom values including your workmail account organization id and workmail account domain.
```
module "prod-account" {
source = "./module"
workmail_org_id = "m-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
workmail_account_domain = "example.com"
account_name = "your_account_name"
password = "your_password"
 }
```
- Set your AWS credentials as environment variables. See [here](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html) for more info.
```
$ export AWS_ACCESS_KEY_ID="anaccesskey"
$ export AWS_SECRET_ACCESS_KEY="asecretkey"
$ export AWS_DEFAULT_REGION="us-west-2"
```
- Run terraform init & then terraform apply. 
```
$ terraform init
$ terraform apply
```
- If you are happy with the plan, proceed and your AWS account will be created.

