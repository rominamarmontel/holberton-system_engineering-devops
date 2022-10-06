# change the ulimit default value to fix the requests failed

exec { 'Update nginx':
    command => 'sed -i s/15/2000/ /etc/default/nginx',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
} ->

exec { 'Restart nginx':
    command => 'sudo service nginx restart',
    path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
