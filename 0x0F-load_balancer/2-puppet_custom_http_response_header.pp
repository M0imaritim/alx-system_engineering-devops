# Configures a brand new ubuntu machine

exec{'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx'
}

$server_hostname = $facts['networking']['hostname']
$custom_header_value = "X-Served-By: ${server_hostname}"

file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => "add_header ${custom_header_value};\n",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_header.conf'],
}
