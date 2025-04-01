#! /usr/bin/env python3
import sys
from scapy.all import *
import urllib.request 



def main():
    #Computer Science(BCS)
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-science-bcs/")
    res = t.stop()
    wrpcap("ComputerScience(BCS).pcap", res)
    
    #Computer Science (BS)
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-science-bs/")
    res = t.stop()
    wrpcap("ComputerScience(BS).pcap", res)
    
    #Computer Science Cyber Operations
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-science-cyber-operations-bs/")
    res = t.stop()
    wrpcap("ComputerScience_Cyber_Operations.pcap", res)
    
    #Cyber Operations
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/cyber-operations-bs/")
    res = t.stop()
    wrpcap("Cyber_Operations.pcap", res)
    
    #Electrical and Computer Engineering
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/electrical-computer-engineering-bs/")
    res = t.stop()
    wrpcap("ElectricalEngineering.pcap", res)
    
    #Big Data
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/big-data-minor/")
    res = t.stop()
    wrpcap("BigData.pcap", res)
    
    #Computer information systems
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-information-systems-minor/")
    res = t.stop()
    wrpcap("ComputerInformationSystems.pcap", res)
    
    #Computer science programming
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-science-programming-minor/")
    res = t.stop()
    wrpcap("ComputerScienceProgramming.pcap", res)
    
    #Cybersecurity
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/cyber-security-minor/")
    res = t.stop()
    wrpcap("Cybersecurity.pcap", res)
    
    #Embedded Systems
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/embedded-systems-minor/")
    res = t.stop()
    wrpcap("EmbeddedSystems.pcap", res)
    
    #Machine Learning
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/machine-learning-minor/")
    res = t.stop()
    wrpcap("MachineLearning.pcap", res)
    
    #Web application development
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/web-application-development-minor/")
    res = t.stop()
    wrpcap("WebApplicationDevelopment.pcap", res)
    
    #Big Data grad
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/big-data-graduate-certificate/")
    res = t.stop()
    wrpcap("BigData_Grad.pcap", res)
    
    #Computer Graphics and Visulization
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-graphics-visualization-graduate-certificate/")
    res = t.stop()
    wrpcap("ComputerGraphicsandVisulization_Grad.pcap", res)
    
    #computer science (MS)
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-science-ms/")
    res = t.stop()
    wrpcap("ComputerScience(MS)_Grad.pcap", res)
    
    #Computer science professional
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/computer-science-professional-mcs/")
    res = t.stop()
    wrpcap("ComputerScienceProfessional_Grad.pcap", res)
    
    #Embedded Systems Grad
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/embedded-systems-graduate-certificate/")
    res = t.stop()
    wrpcap("EmbeddedSystems_Grad.pcap", res)
    
    #Modeling and simulation
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/modeling-simulation-graduate-certificate/")
    res = t.stop()
    wrpcap("ModelingAndSimulation_Grad.pcap", res)
    
    #Network Security
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/network-security-graduate-certificate/")
    res = t.stop()
    wrpcap("NetworkSecurity_Grad.pcap", res)
    
    #parallel cloud computing
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/parallel-cloud-computing-graduate-certificate/")
    res = t.stop()
    wrpcap("ParallelCloudComputing_Grad.pcap", res)
    
    #Non_Degree
    
    
    
    #Contact us
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/contact-us/")
    res = t.stop()
    wrpcap("ContactUs.pcap", res)
    
    #Faculty and Staff
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/faculty-staff/")
    res = t.stop()
    wrpcap("FacultyandStaff.pcap", res)
    
    #Clubs
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/clubs/")
    res = t.stop()
    wrpcap("clubs.pcap", res)
    
    #Scholarships
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/scholarships/")
    res = t.stop()
    wrpcap("scholarships.pcap", res)
    
    #Center for network computing and cybersecurity
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/center-for-network-computing-and-cybersecurity/")
    res = t.stop()
    wrpcap("CenterForNetworking.pcap", res)
    
    #gencyber camp 2023
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://inside.ewu.edu/gencyber/")
    res = t.stop()
    wrpcap("genCyber.pcap", res)
    
    #Learning Outcomes and Statistics
    t = AsyncSniffer(iface="enp0s1")
    t.start()
    s,o = subprocess.getstatusoutput("curl https://www.ewu.edu/cstem/csee/learning-outcomes/")
    res = t.stop()
    wrpcap("LearningOutcomes.pcap", res)
    
    
    


if __name__ == "__main__":
    main()
