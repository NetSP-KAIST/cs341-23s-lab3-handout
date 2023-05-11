set -ex
sudo apt-get update; sudo apt-get -y upgrade
git clone https://github.com/NetSP-KAIST/mininet.git
./mininet/util/install.sh -nfvp
ln -s /vagrant/*.py /home/vagrant/
ln -s /vagrant/controller.py /home/vagrant/pox/pox/misc/
