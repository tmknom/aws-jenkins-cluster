# -*- encoding:utf-8 -*-

from fabric.api import *
from fabric.contrib.console import *


@task
def terraform_plan(resource_dir, tf_vars=''):
    '''terraform planコマンド実行:<resource_name>'''
    execute_terraform(resource_dir, tf_vars, 'plan')


@task
def terraform_plan_destroy(resource_dir, tf_vars=''):
    '''terraform plan -destroyコマンド実行:<resource_name>'''
    execute_terraform(resource_dir, tf_vars, 'plan -destroy')


@task
def terraform_apply(resource_dir, tf_vars=''):
    '''terraform applyコマンド実行:<resource_name>'''
    terraform_plan(resource_dir, tf_vars)
    if not confirm("実行するとリソースを更新します。本当に実行しますか？"):
        abort('リソースの更新を中止しました。')
    execute_terraform(resource_dir, tf_vars, 'apply')


@task
def terraform_destroy(resource_dir, tf_vars=''):
    '''terraform destroyコマンド実行:<resource_name>'''
    terraform_plan_destroy(resource_dir, tf_vars)
    if not confirm("実行するとリソースを破棄します。本当に実行しますか？"):
        abort('リソースの破棄を中止しました。')
    execute_terraform(resource_dir, tf_vars, 'destroy -force')


def execute_terraform(resource_dir, tf_vars, command):
    tf_dir = get_current_dir() + '/' + resource_dir
    with lcd('%s' % (tf_dir)):
        local('%s terraform %s' % (tf_vars, command))


def get_current_dir():
    import os
    return os.path.abspath(os.path.dirname(__file__))
