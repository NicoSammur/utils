# nagiosCheckandRestart.sh
sudo /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
sudo /etc/init.d/nagios restart
