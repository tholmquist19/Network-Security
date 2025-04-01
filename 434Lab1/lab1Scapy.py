#! /usr/bin/env python3

import sys
from socket import *
from urllib.parse import urlparse
from scapy.all import *
import json
import socket
import subprocess, shlex


def main():
    ip = '198.35.26.96'
    ip_p = IP()
    ip_p.dst = ip
    t_p = TCP()
    t_p.seq = 5
    t_p.dport = 80
    t_p.sport = 1234
    t_p.flags="S"
    send_p = ip_p/t_p
    
    #p = send_p.show(dump=True)
    #print(p)
    
    send(send_p)
    send(send_p)
    send(send_p)
    

if __name__ == "__main__":
    main()
