sudo apt-get install python3.8
sudo ln -sT /usr/bin/python3 /usr/bin/python
sudo apt-get install python3-pip
sudo ln -sT /usr/bin/pip3 /usr/bin/pip
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
sudo pip install virtualenv
sudo virtualenv /home/ubuntu/venv/sol
source /home/ubuntu/venv/sol/bin/activate
sudo pip install -r requirements.txt