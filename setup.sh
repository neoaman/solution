sudo apt update
sudo apt -y upgrade
sudo apt-get -y install python3.8
sudo ln -sT /usr/bin/python3 /usr/bin/python
sudo apt install python3-pip
sudo ln -sT /usr/bin/pip3 /usr/bin/pip
sudo apt-get -y install apache2
sudo apt-get -y install libapache2-mod-wsgi-py3
sudo pip3 install virtualenv
sudo su
virtualenv /home/ubuntu/venv/sol
source /home/ubuntu/venv/sol/bin/activate
pip install -r requirements.txt
sudo chown :www-data db.sqlite3
sudo chown www-data:www-data /var/www/solution
python manage.py migrate