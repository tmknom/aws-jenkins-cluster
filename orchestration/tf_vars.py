# -*- encoding:utf-8 -*-

import json
from fabric.api import *

ENVIRONMENT = 'JenkinsCluster'

JENKINS_SUBNET_NAME = 'JenkinsCluster-Public-Subnet-0'

JENKINS_MASTER_TAG = 'JenkinsMaster'
JENKINS_SLAVE_TAG = 'JenkinsSlave'

JENKINS_MASTER_AMI = 'jenkins-master'
JENKINS_SLAVE_AMI = 'jenkins-slave'


def get_jenkins_cluster_tf_vars():
    jenkins_master_ami_id = get_jenkins_master_ami_id()
    jenkins_slave_ami_id = get_jenkins_slave_ami_id()
    jenkins_master_security_group_id = get_jenkins_master_security_group_id()
    jenkins_slave_security_group_id = get_jenkins_slave_security_group_id()
    jenkins_subnet_id = get_jenkins_subnet_id()
    jenkins_key_pair_name = get_jenkins_key_pair_name()
    result = ' TF_VAR_jenkins_master_ami_id=%s' % (jenkins_master_ami_id) \
             + ' TF_VAR_jenkins_slave_ami_id=%s' % (jenkins_slave_ami_id) \
             + ' TF_VAR_jenkins_master_security_group_id=%s' % (jenkins_master_security_group_id) \
             + ' TF_VAR_jenkins_slave_security_group_id=%s' % (jenkins_slave_security_group_id) \
             + ' TF_VAR_jenkins_subnet_id=%s' % (jenkins_subnet_id) \
             + ' TF_VAR_jenkins_key_pair_name=%s' % (jenkins_key_pair_name)
    return result


def get_jenkins_master_ami_id():
    return get_ami_id(JENKINS_MASTER_AMI)


def get_jenkins_slave_ami_id():
    return get_ami_id(JENKINS_SLAVE_AMI)


def get_jenkins_master_security_group_id():
    return get_security_group_id(JENKINS_MASTER_TAG)


def get_jenkins_slave_security_group_id():
    return get_security_group_id(JENKINS_SLAVE_TAG)


def get_jenkins_subnet_id():
    return get_subnet_id(JENKINS_SUBNET_NAME)


def get_jenkins_key_pair_name():
    return get_env('JENKINS_KEY_PAIR_NAME')


def get_ami_id(name):
    region = get_default_region()
    command = "aws ec2 describe-images " \
              + " --region %s " % (region) \
              + " --owners self " \
              + " --filters " \
              + " 'Name=name,Values=%s' " % (name) \
              + " | jq -r '.Images[0].ImageId' "
    result = local(command, capture=True)
    return result


def get_security_group_id(role):
    region = get_default_region()
    command = "aws ec2 describe-security-groups " \
              + " --region %s " % (region) \
              + " --filters " \
              + " 'Name=tag-key,Values=Environment' " \
              + " 'Name=tag-value,Values=%s' " % (ENVIRONMENT) \
              + " 'Name=tag-key,Values=Role' " \
              + " 'Name=tag-value,Values=%s' " % (role) \
              + " | jq -r '.SecurityGroups[].GroupId' "
    result = local(command, capture=True)
    return result


def get_subnet_id(subnet_name):
    region = get_default_region()
    command = "aws ec2 describe-subnets " \
              + " --region %s " % (region) \
              + " --filters " \
              + " 'Name=tag-key,Values=Name' " \
              + " 'Name=tag-value,Values=%s' " % (subnet_name) \
              + " | jq '.Subnets[0].SubnetId' "
    result = local(command, capture=True)
    return json.loads(result)


def get_security_group_tf_vars():
    vpc_id = get_vpc_id(ENVIRONMENT)
    vpc_cidr = get_vpc_cidr(ENVIRONMENT)
    current_ip_address_cidr = get_current_ip_address_cidr()
    ssh_cidr_blocks = get_ssh_cidr_blocks(current_ip_address_cidr, vpc_cidr)
    http_cidr_blocks = get_http_cidr_blocks(current_ip_address_cidr)
    result = ' TF_VAR_vpc_id=%s' % (vpc_id) \
             + ' TF_VAR_ssh_cidr_blocks=%s' % (ssh_cidr_blocks) \
             + ' TF_VAR_http_cidr_blocks=%s' % (http_cidr_blocks)
    return result


def get_ssh_cidr_blocks(current_ip_address_cidr, vpc_cidr):
    return ",".join([current_ip_address_cidr, vpc_cidr])


def get_http_cidr_blocks(current_ip_address_cidr):
    return ",".join([current_ip_address_cidr])


def get_vpc_cidr(environment):
    region = get_default_region()
    command = "aws ec2 describe-vpcs " \
              + " --region %s " % (region) \
              + " --filters " \
              + " 'Name=tag-key,Values=Environment' " \
              + " 'Name=tag-value,Values=%s' " % (environment) \
              + " | jq -r '.Vpcs[0].CidrBlock' "
    result = local(command, capture=True)
    return result


def get_vpc_id(environment):
    region = get_default_region()
    command = "aws ec2 describe-vpcs " \
              + " --region %s " % (region) \
              + " --filters " \
              + " 'Name=tag-key,Values=Environment' " \
              + " 'Name=tag-value,Values=%s' " % (environment) \
              + " | jq -r '.Vpcs[0].VpcId' "
    result = local(command, capture=True)
    return result


def get_default_region():
    command = "aws configure get region"
    result = local(command, capture=True)
    return result


def get_current_ip_address_cidr():
    return get_current_ip_address() + '/32'


def get_current_ip_address():
    import urllib2
    try:
        return urllib2.urlopen('http://inet-ip.info/ip').read()
    except:
        import json
        return json.loads(urllib2.urlopen('http://httpbin.org/ip').read())['origin']


def get_env(key):
    command = "echo $%s" % (key)
    result = local(command, capture=True)
    return result
