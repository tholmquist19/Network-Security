#! /usr/bin/env python3

import sys
from scapy.all import *

def packetMan(packet):
    
    
    pSource = packet[IP].src
    pDest = packet[IP].dst
    pSeq = packet[TCP].seq
    pAck = packet[TCP].ack
    pSrcPrt = packet[TCP].sport
    pFlag = packet[IP].flags
    pLoad = packet[TCP].payload
    pIhl = packet[IP].ihl
    pId = packet[IP].id
    pWindow = packet[0][1].window
    pOptions = packet[TCP].options
    pTFlag = packet[TCP].flags

    
    
    ip_p = IP()
    t_p= TCP()
    ip_p.src = pSource
    ip_p.dst = pDest
    ip_p.ihl = pIhl
    ip_p.id = pId
    ip_p.flags = pFlag
    
    
    
    
    
    t_p.seq = pSeq
    t_p.ack = pAck
    t_p.dport = 80
    t_p.sport = pSrcPrt
    t_p.flags = pTFlag
    t_p.window = pWindow
    t_p.options = pOptions
    send_p = ip_p/t_p
    
    send(send_p/pLoad)


def main():
    cap = sniff(filter ='dst port 8080', prn=packetMan)
    
    
    
if __name__ == "__main__":
    main()
