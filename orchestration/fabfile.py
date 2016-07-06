# -*- encoding:utf-8 -*-

from fabric.api import *
from terraform import *


@task
def build_vpc():
    '''VPC構築'''
    terraform_apply('vpc')


@task
def delete_vpc():
    '''VPC削除'''
    terraform_destroy('vpc')
