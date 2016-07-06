# environment variables
USER_NAME = 'jenkins'
GROUP_NAME = 'jenkins'
HOME_DIR = '/var/lib/jenkins'
SSH_SECRET_KEY_FULL_PATH = ENV['JENKINS_SSH_SECRET_KEY_FULL_PATH']

# Setup ssh
directory "#{HOME_DIR}/.ssh" do
  owner USER_NAME
  group GROUP_NAME
  mode '700'
end

file "#{HOME_DIR}/.ssh/id_rsa" do
  content File.read(SSH_SECRET_KEY_FULL_PATH)
  owner USER_NAME
  group GROUP_NAME
  mode '400'
end
