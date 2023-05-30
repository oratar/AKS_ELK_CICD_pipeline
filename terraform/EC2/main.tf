
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
}

provider "aws" {
  region = var.region
}
data "aws_availability_zones" "available" {}

resource "aws_security_group" "jenkins_secuirty_group" {
  name = var.secuirty_group_name
  dynamic "ingress" {
    for_each    = [8080,50000, 22]
    iterator    = port
    content {
      from_port   = port.value
      to_port     = port.value
      protocol    = "tcp"
      cidr_blocks = port.value == 22 ? ["${var.my_ip}/32"]  : ["0.0.0.0/0"]
  }
}
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "ssh_key" {
  key_name   = var.key_name
  public_key = file("~/.ssh/${var.key_name}.pub")
}

resource "aws_instance" "app_server" {
  ami             = "ami-0cd7ad8676931d727"
  instance_type   = var.instance_type
  key_name      = aws_key_pair.ssh_key.key_name
  root_block_device {
    volume_size = var.volume_size
  }
  security_groups = [aws_security_group.jenkins_secuirty_group.name]
  tags = {
    Name = var.instance_name
  }
user_data=file(var.script)
}

