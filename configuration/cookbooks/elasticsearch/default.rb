package 'https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/rpm/elasticsearch/2.3.2/elasticsearch-2.3.2.rpm' do
  not_if 'rpm -q elasticsearch-2.3.2-1.noarch'
end

execute 'install plugin' do
  command '/usr/share/elasticsearch/bin/plugin install analysis-kuromoji'
  not_if 'test -e /usr/share/elasticsearch/plugins/analysis-kuromoji'
end

service 'elasticsearch' do
  action [:enable, :start]
end
