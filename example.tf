#Module Call
module "example_account" {
source = "./module"
workmail_org_id = "m-xxxxxxxxxxxxxxxxxxxx"
workmail_account_domain = "your_workamil_domain.com"
account_name = "example-name1"
password = "Password1234!"
 }

#Output
output "aws_account_id" {
  value = "${module.example_account.aws_account_id}"
}