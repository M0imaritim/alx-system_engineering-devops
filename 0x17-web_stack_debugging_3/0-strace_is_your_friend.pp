#fixes 500 error code on apache web server

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path     => ['/bin','/usr/bin']
}