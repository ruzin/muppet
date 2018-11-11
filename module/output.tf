#Output AWS Account Id
output "aws_account_id" {
  value = "${aws_organizations_account.new_account.id}"
}