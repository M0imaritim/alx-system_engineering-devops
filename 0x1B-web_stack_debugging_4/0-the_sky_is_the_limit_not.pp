# Manuscript to increase the amount of traffic on an Nginx server

exec {'fixing nginx':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
