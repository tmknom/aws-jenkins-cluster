# -*- encoding:utf-8 -*-

from fabric.api import *
from terraform import *
from tf_vars import *


@task
def build_vpc():
    '''VPC構築'''
    terraform_apply('vpc')


@task
def delete_vpc():
    '''VPC削除'''
    terraform_destroy('vpc')


@task
def build_security_group():
    '''セキュリティグループ構築'''
    tf_vars = get_security_group_tf_vars()
    terraform_apply('security_group', tf_vars)


@task
def delete_security_group():
    '''セキュリティグループ削除'''
    tf_vars = get_security_group_tf_vars()
    terraform_destroy('security_group', tf_vars)
