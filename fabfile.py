# -*- encoding:utf-8 -*-

from configuration.fabfile import itamae_base
from configuration.fabfile import itamae_jenkins_base
from configuration.fabfile import itamae_jenkins_master
from configuration.fabfile import itamae_jenkins_slave
from orchestration.fabfile import build_vpc
from orchestration.fabfile import delete_vpc
from orchestration.fabfile import build_security_group
from orchestration.fabfile import delete_security_group
from orchestration.fabfile import build_ec2
from orchestration.fabfile import delete_ec2
from operation.jenkins.fabfile import describe_jenkins_addresses
from operation.jenkins.fabfile import describe_initial_admin_password
