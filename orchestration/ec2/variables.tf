variable "jenkins_master_ami_id" {
}

variable "jenkins_slave_ami_id" {
}

variable "jenkins_master_security_group_id" {
}

variable "jenkins_slave_security_group_id" {
}

variable "jenkins_subnet_id" {
}

variable "jenkins_key_pair_name" {
}

variable "jenkins_slave_count" {
  default = "2"
}

variable "jenkins_master_instance_type" {
  default = "t2.micro"
}

variable "jenkins_slave_instance_type" {
  default = "t2.medium"
}

variable "jenkins_volume_size" {
  default = "8"
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
