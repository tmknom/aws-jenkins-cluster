# security
include_recipe '../cookbooks/sudo/default.rb'
include_recipe '../cookbooks/sshd/default.rb'

# rpm
include_recipe '../cookbooks/rpm_repository/default.rb'
include_recipe '../cookbooks/rpm_package/default.rb'
include_recipe '../cookbooks/rpm_package/update.rb'
