resource "aws_security_group" "jenkins_master" {
  name = "${var.environment}-${var.jenkins_master}-SecurityGroup"

  ingress {
    from_port = "${var.ssh_port}"
    to_port = "${var.ssh_port}"
    protocol = "${var.tcp}"
    cidr_blocks = ["${split(",", var.ssh_cidr_blocks)}"]
  }

  ingress {
    from_port = "${var.http_port}"
    to_port = "${var.http_port}"
    protocol = "${var.tcp}"
    cidr_blocks = ["${split(",", var.http_cidr_blocks)}"]
  }

  egress {
    from_port = 0
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
    protocol = "-1"
  }

  vpc_id = "${var.vpc_id}"
  description = "allow http and ssh"

  tags {
    Name = "${var.environment}-${var.jenkins_master}-SecurityGroup"
    Role = "${var.jenkins_master}"
    Environment = "${var.environment}"
  }
}

resource "aws_security_group" "jenkins_slave" {
  name = "${var.environment}-${var.jenkins_slave}-SecurityGroup"

  ingress {
    from_port = "${var.ssh_port}"
    to_port = "${var.ssh_port}"
    protocol = "${var.tcp}"
    cidr_blocks = ["${split(",", var.ssh_cidr_blocks)}"]
  }

  egress {
    from_port = 0
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
    protocol = "-1"
  }

  vpc_id = "${var.vpc_id}"
  description = "allow ssh"

  tags {
    Name = "${var.environment}-${var.jenkins_slave}-SecurityGroup"
    Role = "${var.jenkins_slave}"
    Environment = "${var.environment}"
  }
}
