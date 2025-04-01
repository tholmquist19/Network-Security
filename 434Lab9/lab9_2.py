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
                ind = k
    st = b''
    for p in p[ind]:
        if Raw in p:
            st += p[TCP].payload.load
            
    of = open("out.txt", "wb")
    of.write(st)
    of.close()
    
    file_size = os.path.getsize('out.txt')
    file_size = file_size/1000
    
    
    
    #second pcap
    
    ind2 = ''
    isBreak = False
    for k,v in p2.items():
        if isBreak:
            break
        if k.startswith("TCP") and not(k.endswith(":443")):
            li = k.split(".")
            if len(li)==7:
                ind2 = k
                for p in p2[ind2]:
                    if Raw in p:
                        st2 = b''
                        for p in p2[ind2]:
                            if Raw in p:
                                st2 += p[TCP].payload.load
            
                        of = open("out2.txt", "wb")
                        of.write(st2)
                        of.close()
                        file_size2 = os.path.getsize('out2.txt')
                        if file_size2 > 100000:
                            isBreak = True;
                            break
    file_size2 = file_size2/1000
    
    
    same = False
    comp = False
    comp2 = False
    if file_size-file_size2<1.5 and file_size-file_size2>0:
        comp = True
    if file_size2-file_size<1.5 and file_size2-file_size>0:
        comp2 = True
    if comp or comp2:
        same = True
    return same

def main():
    pr = ''
    pr2 = ''
    p2 = rdpcap(sys.argv[1]).sessions()
    path = sys.argv[1]
    p = rdpcap("BigData.pcap").sessions()
    #compare
    same = compare(p,p2)
    if same:
        pr = "Big Data"
        
        
        
    if not path.startswith("non"):
        p = rdpcap("BigData_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Big Data Grad"
            else:
                pr = "Big Data Grad"
            
            
        p = rdpcap("ComputerGraphicsandVisulization_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Graphic and Visulization"
            else:
                pr = "Computer Graphic and Visulization"
            
            
        p = rdpcap("ComputerScience(BCS).pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Science(BCS)"
            else:
                pr = "Computer Science(BCS)"
            
            
        p = rdpcap("ComputerScience(BS).pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Science(BS)"
            else:
                pr = "Computer Science(BS)"
            
            
        p = rdpcap("ComputerScience_Cyber_Operations.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Science Cyber Operations"
            else:
                pr = "Computer Science Cyber Operations"
            
            
        p = rdpcap("Cyber_Operations.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Cyber Operations"
            else:
                pr = "Cyber Operations"
        
            
        p = rdpcap("ElectricalEngineering.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Electrical Engineering"
            else:
                pr = "Electrical Engineering"
            
            
        p = rdpcap("ComputerInformationSystems.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Information Systems"
            else:
                pr = "Computer Information Systems"
            
            
        p = rdpcap("ComputerScienceProgramming.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Science Programming"
            else:
                pr = "Computer Science Programming"
            
            
        p = rdpcap("Cybersecurity.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Cyber Security"
            else:
                pr = "Cyber Security"
            
            
        p = rdpcap("EmbeddedSystems.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Embedded Systems"
            else:
                pr = "Embedded Systems"
            
            
        p = rdpcap("MachineLearning.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Machine Learning"
            else:
                pr = "Machine Learning"
            
            
        p = rdpcap("WebApplicationDevelopment.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Web Application Development"
            else:
                pr = "Web Application Development"
            
            
        p = rdpcap("ComputerScience(MS)_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Science(MS) Grad"
            else:
                pr = "Computer Science(MS) Grad"
            
            
        p = rdpcap("ComputerScienceProfessional_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Computer Science Professional Grad"
            else:
                pr = "Computer Science Professional Grad"
            
            
        p = rdpcap("EmbeddedSystems_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Embedded Systems Grad"
            else:
                pr = "Embedded Systems Grad"
            
            
        p = rdpcap("ModelingAndSimulation_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Modeling and Simulation Grad"
            else:
                pr = "Modeling and Simulation Grad"
            
            
        p = rdpcap("NetworkSecurity_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Network Security Grad"
            else:
                pr = "Network Security Grad"
            
            
        p = rdpcap("ParallelCloudComputing_Grad.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Parallel Cloud Computing Grad"
            else:
                pr = "Parallel Cloud Computing Grad"
        
        
        
    else:
        p = rdpcap("ContactUs.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Contact Us"
            else:
                pr = "Contact Us"
            
        p = rdpcap("FacultyandStaff.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Faculty and Staff"
            else:
                pr = "Faculty and Staff"
            
        p = rdpcap("clubs.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Clubs"
            else:
                pr = "Clubs"
            
        p = rdpcap("scholarships.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Scholarships"
            else:
                pr = "Scholarships"
            
        p = rdpcap("CenterForNetworking.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Center for Network Computing and Cybersecurity"
            else:
                pr = "Center for Network Computing and Cybersecurity"
            
        p = rdpcap("genCyber.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Gencyber Camp 2023"
            else:
                pr = "Gencyber Camp 2023"
            
        p = rdpcap("LearningOutcomes.pcap").sessions()
        #compare
        same = compare(p,p2)
        if same:
            if pr != '':
                pr2 = " or Learning Outcomes and Statistics"
            else:
                pr = "Learning Outcomes and Statistics"
    
    print(pr)
    if pr2 != '':
        print(pr2)
        
    
        
    

    
if __name__ == "__main__":
    main()
