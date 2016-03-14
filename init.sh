sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo kill $(ps ax | grep "gunicorn" | awk '{print $1}')
cd /home/box/web/
gunicorn -b 0.0.0.0:8080 hello:wsgi_app -D
sudo ln -s /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/ask.conf
sudo /etc/init.d/gunicorn restart
