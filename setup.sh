sudo apt update
sudo apt -y upgrade
sudo apt-get -y install python3.8
sudo ln -sT /usr/bin/python3 /usr/bin/python
sudo apt -y install python3-pip
sudo ln -sT /usr/bin/pip3 /usr/bin/pip
sudo apt-get -y install apache2
sudo apt-get -y install libapache2-mod-wsgi-py3
sudo pip3 install virtualenv
virtualenv /home/ubuntu/venv/sol
source /home/ubuntu/venv/sol/bin/activate
pip install -r requirements.txt
sudo chown www-data:www-data db.sqlite3
sudo chown www-data:www-data /var/www/solution
sudo chown www-data:www-data /var/www/solution/
sudo chown www-data:www-data /var/www/solution/*
python manage.py migrate
cp custom.conf /etc/apache2/sites-available/
cd /etc/apache2/sites-available/
a2ensite custom.conf
a2dissite default-ssl.conf
a2dissite 000-default.conf
service apache2 restart