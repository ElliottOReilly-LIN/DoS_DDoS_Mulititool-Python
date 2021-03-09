# Author: Elliott O'Reilly - 09 March 2021
# Cyber Security CMP3750 ASS1 Item-1
from scapy.all import *
import socket
import struct


def dosDetect():
    # Open up the socket libraries to capture packets
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)

    ipArray = []  # An empty array for the IPs
    uniqueArray = []
    # The following line of code will open a text file, piping
    # details of DDoS attack in append mode.

    file_txt = open("attack_DDoS.txt", 'w')  # Begin a log text file
    t1 = str(datetime.now())  # Grab the current time for log purposes
    file_txt.writelines(t1)
    file_txt.writelines("\n")

    # if a particular IP is hitting for more than 15 times then it is an attack.
    countIP = 0
    while True:
        pkt = s.recvfrom(2048)  # This port can be used from machine to machine
        ipheader = pkt[0][14:34]
        ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
        IP = socket.inet_ntoa(ip_hdr[3])
        '''inet_ntoa(packed_ip) -> ip_address_string
                Convert an IP address from 32-bit packed
                binary format to string format'''
        ipArray.append(IP)
        if IP not in uniqueArray:
            uniqueArray.append(IP)
            countIP = countIP + 1
            print("count: ", countIP)
        # Some verbose shell output here
        print("The Source of the IP is:", IP)
        # Break out of the loop here if 15 consecutive hits
        if (countIP >= 15 and IP != "127.0.0.1"):
            # Disregard the Loopback address and test on 15 hits
            break

    consecHit = 0
    for i in range(1, len(ipARrray)):
        # Test here for consecutive IP hits, disregarding the Loop back address
        if(ipArray[i] == ipArray[i - 1]) and (ipARrray[i] != "127.0.0.1"):
            consecHit = consecHit + 1

            print("in here", ipARrray[i], end=" ")
    # Write out logs to the text file
    if consecHit > 10:
        line = "\n\n15 His exceeded: ", "\n", "IP Adreess: ", IP, "\n", "At time: ", t1, "\n"
        file_txt.writelines(line)
        line = "DDOS attack is Detected: \n"
        file_txt.writelines(line)
        line = "IP Address: "
        file_txt.writelines(line)
        file_txt.writelines(IP)
        file_txt.writelines("\n")
