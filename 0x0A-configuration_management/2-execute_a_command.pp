# kills a process named killmenow
exec { 'pkill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
