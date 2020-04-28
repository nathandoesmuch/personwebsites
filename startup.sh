#!/bin/sh
sudo apt-get update
sudo apt-get install python-pip python-dev nginx --yes < "/dev/null"
sudo pip install virtualenv
mkdir ~/application
cd ~/application
sudo git clone https://github.com/nathandoesmuch/personalwebsites.git ~/application
virtualenv libraries
source libraries/bin/activate
pip install uwsgi flask
sudo bash -c "cat > /etc/systemd/system/personalwebsites.service" <<EOF
[Unit]
Description=Personal Websites
After=network.target

[Service]
User=nmoore8763
Group=www-data
WorkingDirectory=/home/nmoore8763/application
Environment="PATH=/home/nmoore8763/application/libraries/bin"
ExecStart=/home/nmoore8763/application/libraries/bin/uwsgi --ini personalwebsites.ini

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl start personalwebsites
sudo systemctl enable personalwebsites
sudo bash -c "cat > /etc/nginx/sites-available/personalwebsites" <<EOF
server {
    listen 80 default_server;
    server_name _;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/nmoore8763/application/personalwebsites.sock;
    }
}
EOF
sudo ln -s /etc/nginx/sites-available/personalwebsites /etc/nginx/sites-enabled
sudo systemctl restart nginx


