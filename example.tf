#Module Call
module "example_account" {
source = "./module"
workmail_org_id = "m-xxxxxxxxxxxxxxxxxx"
workmail_account_domain = "your-domain.com"
account_name = "example-name"
password = "Password1234!"
 }

#Output
output "aws_account_id" {
  value = "${module.example_account.aws_account_id}"
}