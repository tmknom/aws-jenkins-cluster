include_recipe 'base.rb'

# app
include_recipe '../cookbooks/rpm_package/app.rb'
include_recipe '../cookbooks/mysql_client/default.rb'
include_recipe '../cookbooks/mysql_server/default.rb'
include_recipe '../cookbooks/memcached/default.rb'
include_recipe '../cookbooks/nodejs/default.rb'
include_recipe '../cookbooks/ruby/default.rb'
