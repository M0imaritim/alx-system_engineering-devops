#fixes 500 error code on apache web server

file_line { 'fix_php_typo':
  path    => '/var/www/html/wp-settings.php',  # Target file
  match   => 'phpp',
  line    => 'php',
  replace => true,
}