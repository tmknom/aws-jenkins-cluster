variable "vpc_id" {
}

variable "ssh_cidr_blocks" {
}

variable "http_cidr_blocks" {
}

variable "ssh_port" {
  default = "22"
}

variable "http_port" {
  default = "8080"
}

variable "tcp" {
  default = "tcp"
}

variable "jenkins_master" {
  default = "JenkinsMaster"
}

variable "jenkins_slave" {
  default = "JenkinsSlave"
}

variable "environment" {
  default = "JenkinsCluster"
}
