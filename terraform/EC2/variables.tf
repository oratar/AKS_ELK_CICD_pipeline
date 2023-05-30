variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "jenkins_server"
}

variable "secuirty_group_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "jenkins_security_group"
}

variable "region" {
  description = "Value of the aws region"
  type        = string
  default     = "ap-northeast-1"
}

variable "instance_type" {
  description = "Value of the instance type"
  type        = string
  default     = "t2.medium"
}

variable "my_ip" {
  description = "Value of the your public ip"
  type        = string
  default     = "213.57.121.34"
}

variable "volume_size" {
  description = "Value of the volume size"
  type        = number
  default     = 8
}
variable "key_name" {
  description = "name of key pair name"
  type        = string
  default     = "jenkins_keys"
}

variable "script" {
  description = "name of the script"
  type        = string
}



