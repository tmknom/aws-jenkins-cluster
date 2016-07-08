LOCALTIME_CONFIG = '/etc/localtime'
CLOCK_CONFIG = '/etc/sysconfig/clock'

execute 'set timezone Asia/Tokyo' do
  # http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/set-time.html
  not_if "cat #{CLOCK_CONFIG} | grep '^ZONE=\"Asia\\/Tokyo\"'"
  command <<-EOL
    ln -sf /usr/share/zoneinfo/Asia/Tokyo #{LOCALTIME_CONFIG}
    sed -i 's/^ZONE=\"UTC\"/ZONE=\"Asia\\/Tokyo\"/' #{CLOCK_CONFIG}
    sed -i 's/^UTC=true/UTC=false/' #{CLOCK_CONFIG}
  EOL
end
