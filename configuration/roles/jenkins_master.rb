include_recipe 'jenkins_base.rb'

# jenkins
include_recipe '../cookbooks/jenkins/default.rb'
include_recipe '../cookbooks/user/jenkins_master.rb'
include_recipe '../cookbooks/swap/default.rb'
