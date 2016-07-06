resource "aws_instance" "jenkins_master" {
  ami = "${var.jenkins_master_ami_id}"
  subnet_id = "${var.jenkins_subnet_id}"
  instance_type = "${var.instance_type}"
  key_name = "${var.jenkins_key_pair_name}"
  vpc_security_group_ids = [
    "${var.jenkins_master_security_group_id}",
  ]

  associate_public_ip_address = true
  disable_api_termination = false

  root_block_device {
    volume_size = "${var.jenkins_volume_size}"
    volume_type = "gp2"
    delete_on_termination = true
  }

  tags {
    Name = "${var.environment}-${var.jenkins_master}"

    Environment = "${var.environment}"
    Role = "${var.jenkins_master}"
  }
}

resource "aws_instance" "jenkins_slave" {
  count = "${var.jenkins_slave_count}"

  ami = "${var.jenkins_slave_ami_id}"
  subnet_id = "${var.jenkins_subnet_id}"
  instance_type = "${var.instance_type}"
  key_name = "${var.jenkins_key_pair_name}"
  vpc_security_group_ids = [
    "${var.jenkins_slave_security_group_id}",
  ]

  associate_public_ip_address = true
  disable_api_termination = false

  root_block_device {
    volume_size = "${var.jenkins_volume_size}"
    volume_type = "gp2"
    delete_on_termination = true
  }

  tags {
    Name = "${var.environment}-${var.jenkins_slave}-${count.index}"

    Environment = "${var.environment}"
    Role = "${var.jenkins_slave}"
  }
}
