# change the ulimit default value to fix the requests failed

exec { 'Update nginx':
    path    => [ '/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/' ],
    command => 'sed -i s/15/2000/ /etc/default/nginx'
}

exec { 'Restart nginx':
    path    => [ '/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/' ],
    command => 'sudo service nginx restart'
}
