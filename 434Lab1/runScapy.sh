#! /usr/bin/bash
#sudo iptables -I OUTPUT -p tcp --tcp-flags ALL RST -j DROP

sudo ./lab1Scapy.py

#sudo iptables -D OUTPUT -p tcp --tcp-flags ALL RST -j DROP
