#! /usr/bin/env python3
import sys
from scapy.all import *



def main():
    #p = rdpcap("/home/tholmquist/Downloads/434Lab6/home/cannontcpdumps/injector_traceroute.tcpdump")
    p = rdpcap(sys.argv[1])
    counter = 0
    i = 0
    a = [0]*3
    while i < len(p)-1:
        check = p[i+1].ttl - p[i].ttl
        if check==1:
            j=0
            while check == 1:
                a[j] = p[i].ttl
                j += 1
                check = p[i+1].ttl - p[i].ttl  
                i+=1
            counter += 1
            print(a)
        i+=1
    print(counter)


if __name__ == "__main__":
    main()
