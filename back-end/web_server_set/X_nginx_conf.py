NG = """
# the upstream component nginx needs to connect to
upstream $_django {
    server unix:///home/wwwroot/$/@.sock; # for a file socket
    # server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}
# configuration of the server
server {
    # the port your site will be served on
    listen      8091;
    # the domain name it will serve for
    server_name 222.197.183.157; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /home/wwwroot/$/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /home/wwwroot/$/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  $_django;
        include     /home/wwwroot/$/uwsgi_params; # the uwsgi_params file you installed
    }
}
"""