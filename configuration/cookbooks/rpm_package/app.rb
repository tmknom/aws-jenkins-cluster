package 'http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm' do
  not_if 'rpm -q groonga-release'
end

%w(mecab mecab-ipadic nginx libxml2-devel libxslt-devel ImageMagick-devel patch).each do |pkg|
  package pkg
end
