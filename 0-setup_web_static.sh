#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static

html_content="<html><body><h1>Hello, world!</h1></body></html>"
html_file="/data/web_static/releases/test/index.html"

sudo apt update
sudo apt install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

echo "$html_content" > "$html_file"
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
