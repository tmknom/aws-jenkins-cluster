# environment variables
USER_NAME = 'jenkins_slave'
GROUP_NAME = 'jenkins_slave'
HOME_DIR = '/home/jenkins_slave'
SSH_PUBLIC_KEY_FULL_PATH = ENV['JENKINS_SSH_PUBLIC_KEY_FULL_PATH']

# user setting
user USER_NAME do
  home HOME_DIR
end

# Setup ssh
directory "#{HOME_DIR}/.ssh" do
  owner USER_NAME
  group GROUP_NAME
  mode '700'
end

file "#{HOME_DIR}/.ssh/authorized_keys" do
  content File.read(SSH_PUBLIC_KEY_FULL_PATH)
  owner USER_NAME
  group GROUP_NAME
  mode '600'
end
