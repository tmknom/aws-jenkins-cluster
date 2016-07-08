package 'http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm' do
  not_if 'rpm -q mysql-community-release'
end

%w(mysql-community-client mysql-community-devel mysql-community-server mysql-utilities).each do |pkg|
  package pkg
end

remote_file '/etc/my.cnf' do
  source 'files/etc/my.cnf'
  owner 'root'
  group 'root'
  mode '0644'
end

service 'mysqld' do
  action [:enable, :start]
end
