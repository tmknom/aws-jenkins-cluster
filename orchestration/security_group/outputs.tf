output "jenkins_master_id" {
  value = "${aws_security_group.jenkins_master.id}"
}

output "jenkins_master_name" {
  value = "${aws_security_group.jenkins_master.name}"
}

output "jenkins_slave_id" {
  value = "${aws_security_group.jenkins_slave.id}"
}

output "jenkins_slave_name" {
  value = "${aws_security_group.jenkins_slave.name}"
}
