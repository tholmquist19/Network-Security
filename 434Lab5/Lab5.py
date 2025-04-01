#! /usr/bin/env python3
import sys
from scapy.all import *

def main():

    
    notFound = True
    pingr = IP(dst=sys.argv[1])/ICMP()
    ip = pingr.src
    li = list(ip.split("."))
    lastNum = int(li[3])
    lastNum += 1
    ip = li[0]+'.'+li[1]+'.'+li[2]+'.'+str(lastNum)
    pingr2 = IP(dst=sys.argv[1],src=ip)/ICMP()
    
    
    #FreeBSD check
    tracker = 0
    for i in range(10):
        capt = sr1(pingr)
        for i in range(10):
            send(pingr2)
        capt2 = sr1(pingr)
        gap = capt2.id-capt.id
        if gap>=8 and gap<=12:
            tracker += 1
        print(gap)
    if tracker>=5:
        print("\n\nThe OS is probably FreeBSD\n\n")
        notFound = False
    
    
    #Linux check
    if notFound:
        tracker = 0
        for i in range(10):
            capt3 = sr1(pingr)
            send(pingr2)
            capt4 = sr1(pingr)
            gap = capt4.id-capt3.id
            gap2 = capt3.chksum - capt4.chksum 
            if gap2 < 25 and gap2>0:
                tracker += 1
        if tracker >= 9:
            print("\n\nThe OS is probably Linux\n\n")
            notFound = False
    
    if notFound:
        print("\n\nOS was not found\n\n")
    


if __name__ == "__main__":
    main()
