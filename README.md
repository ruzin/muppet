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

Getting Started & Documentation
-------------------------------
Muppet is very simple to use, hence the name :P. To get started:
- Clone the repository locally
- In example.tf

