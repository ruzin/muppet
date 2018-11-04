terraform {
  backend "local" {
    path = "./org.tfstate"
  }
}

provider "aws" {
  region     = "eu-west-1"
}