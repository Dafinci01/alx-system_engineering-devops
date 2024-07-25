#this is for ssh into server using puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => '
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ',
}

