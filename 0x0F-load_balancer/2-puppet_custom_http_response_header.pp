#!/usr/bin/env bash
#task of creating a custom HTTP header response, but with Puppet

exec { 'update':
  command => 'apt-get update',
  path    => ['/bin', '/usr/bin/'],
  before  => Exec['install_nginx'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }
}

server_tokens off;

add_header X-Served-By $hostname;

",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}
