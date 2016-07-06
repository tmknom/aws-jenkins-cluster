execute 'download repository' do
  command 'wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo; rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key'
  not_if 'test -e /etc/yum.repos.d/jenkins.repo'
end

package 'jenkins'

service 'jenkins' do
  action [:enable, :start]
end
