variable "environment" {
  default = "JenkinsCluster"
}

variable "vpc_cidr" {
  default = "192.168.0.0/16"
}

variable "availability_zones" {
  default = "ap-northeast-1a,ap-northeast-1c"
}

variable "public_subnets" {
  default = "192.168.1.0/24,192.168.2.0/24"
}

variable "private_subnets" {
  default = ""
}

variable "public_network" {
  default = "Public"
}

variable "private_network" {
  default = "Private"
}

variable "enable_dns_hostnames" {
  default = true
}

variable "enable_dns_support" {
  default = true
}

variable "default_route" {
  default = "0.0.0.0/0"
}
