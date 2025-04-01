#! /usr/bin/env python3
import sys
from scapy.all import *
import urllib.request 
import subprocess
import os

def compare(p, p2):
    #first pcap
        
    ind = ''
    for k,v in p.items():
        if k.startswith("TCP") and not(k.endswith(":443")):
            li = k.split(".")
            if len(li)==7:
                #print(k)
                ind = k
    st = b''
    for p in p[ind]:
        if Raw in p:
            #p.show()
            st += p[TCP].payload.load
            
    of = open("out.txt", "wb")
    of.write(st)
    of.close()
    
    file_size = os.path.getsize('out.txt')
    print("File Size is :", file_size, "bytes")
    
    
    
    #second pcap
    
    ind2 = ''
    for k,v in p2.items():
        if k.startswith("TCP") and not(k.endswith(":443")):
            li = k.split(".")
            if len(li)==7:
                print(k)
                ind2 = k
    st2 = b''
    for p in p2[ind2]:
        if Raw in p:
            p.show()
            st2 += p[TCP].payload.load
    print(st2)
            
    of = open("out2.txt", "wb")
    of.write(st2)
    of.close()
    
    file_size2 = os.path.getsize('out2.txt')
    print("File2 Size is :", file_size2, "bytes")
    print("\n\n")
    
    
    same = False
    comp = False
    comp2 = False
    if file_size-file_size2<30 and file_size-file_size2>0:
        comp = True
    if file_size2-file_size<30 and file_size2-file_size>0:
        comp2 = True
    if comp or comp2:
        same = True
    return same

def main():
    p2 = rdpcap(sys.argv[1]).sessions()
    for _ in range(1):
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/BigData.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Big Data")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/BigData_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Big Data Grad")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerGraphicsandVisulization_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Graphic and Visulization")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerScience(BCS).pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Science(BCS)")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerScience(BS).pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Science(BS)")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerScience_Cyber_Operations.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Science Cyber Operations")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/Cyber_Operations.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Cyber Operations")
        
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ElectricalEngineering.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Electrical Engineering")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerInformationSystems.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Information Systems")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerScienceProgramming.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Science Programming")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/Cybersecurity.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Cyber Security")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/EmbeddedSystems.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Embedded Systems")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/MachineLearning.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Machine Learning")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/WebApplicationDevelopment.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Web Application Development")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerScience(MS)_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Science(MS) Grad")
            break
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ComputerScienceProfessional_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Computer Science Professional Grad")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/EmbeddedSystems_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Embedded Systems Grad")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ModelingAndSimulation_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Modeling and Simulation Grad")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/NetworkSecurity_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Network Security Grad")
            
            
        p = rdpcap("/home/tholmquist/Downloads/434Lab9/ParallelCloudComputing_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            print("Parallel Cloud Computing Grad")
            
        
    
    
if __name__ == "__main__":
    main()
