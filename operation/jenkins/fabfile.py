# -*- encoding:utf-8 -*-

from fabric.api import *


@task
def describe_jenkins_addresses():
    '''Jenkins サーバのIPアドレスの取得'''
    command = "aws ec2 describe-instances " \
              + " --filters " \
              + " 'Name=tag-key,Values=Environment' " \
              + " 'Name=tag-value,Values=JenkinsCluster' " \
              + " | jq '.Reservations[].Instances[] " \
              + " | {Name: (.Tags[] | select(.Key==\"Name\").Value), PublicIpAddress: select(.PublicIpAddress!=null).PublicIpAddress, PrivateIpAddress}' "
    local(command)


@task
def describe_initial_admin_password():
    '''initialAdminPassword の取得 -H <ip_address>'''
    sudo('cat /var/lib/jenkins/secrets/initialAdminPassword')
