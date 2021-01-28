import scapy.all as scapy
import sys

ip = sys.argv[1]
arpRequest = scapy.ARP(pdst = ip)
broadcastP = scapy.Ether(dst = "ff:ff:ff:ff:ff")
arpReqBroad = broadcastP/arpRequest
answ, unansw = scapy.srp(arpReqBroad, timeout = 1)
print(answ.summary())
print(unansw.summary())