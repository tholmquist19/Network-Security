#! /usr/bin/env python3
import sys
from scapy.all import *



def main():
    p = rdpcap(sys.argv[1])
    a = []
    pSave = None
    
    
    for i in range(len(p)):
        pi = p[i]
        if Raw in pi:
            pload = pi[TCP].payload.load.decode('latin-1')
        se = int(p[i].seq)
        a.append(se)
        aLength = len(a)
        for j in range(aLength-1):
            if se==a[j]:
                pj = p[j]
                if Raw in pj:
                    pload2 = pj[TCP].payload.load.decode('latin-1')
                    pload = pload.lower()
                    pload2 = pload2.lower()
                    if pload.startswith("http") and pload2.startswith("http") and pload!=pload2:
                        pSave = p[j]
                        print(j+1)
                        break
    if pSave != None:
        pSave.show()
    else:
        print("You're safe from shooters")
        
    


if __name__ == "__main__":
    main()
