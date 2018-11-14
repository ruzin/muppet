#Null resource with local exec provisioner to create workmail user.

resource "null_resource" "create_workmail_user" {
  provisioner "local-exec" {
    command = "python ./module/scripts/create_workmail_user.py"

      environment {
      user_name = "${lower(var.account_name)}"
      password = "${var.password}"
      email    = "${lower(var.account_name)}@${var.workmail_account_domain}"
      workmail_org_id = "${var.workmail_org_id}"
    }
  }
}


# Create aws account in the organization
resource "aws_organizations_account" "new_account" {
  name  = "${var.account_name}"
  email = "${lower(var.account_name)}@${lower(var.workmail_account_domain)}"
}
