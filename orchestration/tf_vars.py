# -*- encoding:utf-8 -*-

import json
from fabric.api import *

ENVIRONMENT = 'JenkinsCluster'


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
