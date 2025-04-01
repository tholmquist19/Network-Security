sudo iptables -I OUTPUT -p tcp --tcp-flags ALL RST,ACK -j DROP
sudo iptables -I INPUT -p tcp --tcp-flags ALL RST -j DROP
sudo iptables -I INPUT -p tcp --tcp-flags ALL RST,ACK -j DROP

sudo ./lab2.py
