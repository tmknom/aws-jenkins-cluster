# -*- encoding:utf-8 -*-

from fabric.api import *

BASE_ROLE = 'base'

EC2_USER = 'ec2-user'
DEFAULT_SSH_PORT = '22'


@task
def itamae_base():
    '''base コンフィギュレーション（初回） -H <ip_address>'''
    execute_itamae(
        BASE_ROLE,
        EC2_USER,
        DEFAULT_SSH_PORT,
        get_env('SSH_INITIALIZE_KEY_PATH')
    )


def execute_itamae(role, user_name, ssh_port, ssh_key_path):
    command = "time bundle exec itamae ssh " \
              + " roles/%s.rb " % (role) \
              + " -u %s " % (user_name) \
              + " -p %s " % (ssh_port) \
              + " -i %s " % (ssh_key_path) \
              + " -h %s " % (env.hosts[0])
    with lcd(get_current_dir()):
        local(command)


def get_env(key):
    command = "echo $%s" % (key)
    result = local(command, capture=True)
    return result


def get_current_dir():
    import os
    return os.path.abspath(os.path.dirname(__file__))
