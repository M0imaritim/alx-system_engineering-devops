# setting up config using puppet
file { '/etc/ssh/ssh_config':
  ensure  => file,
    content => "\
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
}
