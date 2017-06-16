#!/usr/bin/env bash
ln -s /home/www/nlp/nlp_nginx.conf /etc/nginx/conf.d/
source ~/.bash_profile
pyenv local 2.7.12

cd /home/www/nlp
pip install -r requirements.txt

python /home/www/nlp/manage.py collectstatic  --noinput
kill -9 `cat /tmp/nlp.pid`
uwsgi --ini /home/www/nlp/uwsgi.ini

#service nginx stop
#service nginx start
sudo /etc/init.d/nginx reload