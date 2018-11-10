# Muppet
## Description
Muppet is a combination of python/terraform scripts that fully automates and version controls AWS account creation.

Core Components
-------------------------------
The core components of muppet are:

- **[AWS Workmail](https://aws.amazon.com/workmail/)**: Muppet uses the workmail API to automate the create of email accounts, a requirement when creating an AWS account.
- **[Terraform](https://www.terraform.io/)**: Muppet uses Terraform to create the AWS account in AWS Organizations and store the config state. In the near future, the goal is to configure workmail via terraform as well.
- **[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)**: Muppet used Boto3, the AWS python SDK, to create email accounts in AWS workmail.

Pre-requisites
-------------------------------
Prior to using Muppet, the following pre-requisites need to be in place:

- **[AWS Workmail](https://aws.amazon.com/workmail/)**: Create an AWS workmail account. The first 25 users are free to create and then its $4 per user per month.
- **Terraform/Boto3**: Ensure that you have installed terraform/boto3 in the environment that you are running Muppet in.

Getting Started & Documentation
-------------------------------

