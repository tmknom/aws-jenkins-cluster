CLOUD_INIT_CONFIG = '/etc/cloud/cloud.cfg'
I18N_CONFIG = '/etc/sysconfig/i18n'

execute 'set locale ja_JP' do
  not_if "cat #{CLOUD_INIT_CONFIG} | grep '^locale: ja_JP.UTF-8'"
  command <<-EOL
    echo 'locale: ja_JP.UTF-8' >> #{CLOUD_INIT_CONFIG}
    sed -i 's/en_US/ja_JP/' #{I18N_CONFIG}
  EOL
end
