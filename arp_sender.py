from scapy.layers.l2 import ARP, Ether
import sys
import logging

from scapy.sendrecv import srp

import encode_decode
import encrypt_decrypt

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def create_mac_list(hex_list: list, channel: str):
    """
    Create a List of mac-addresses out of the List with Hex-Data from Data-Encoding
    :param hex_list: return list from Encoding-Function
    :return: List of Hex-Data in Mac-Format
    """
    #print(hex_list)
    mac_count = len(hex_list) // 3
    mac_rest = len(hex_list) % 3
    mac_list = []

    for i in range(mac_count):
        mac = hex_list[i*3:(i+1)*3]
        mac.insert(0, channel)
        mac.insert(1, "ff")
        mac.insert(2, "01")
        mac_list.append(mac)

    if mac_rest > 0:
        last_mac = hex_list[len(hex_list)-mac_rest:len(hex_list)]

        for i in range(3 - mac_rest):
            last_mac.insert(0,"00")
        last_mac.insert(0, channel)
        last_mac.insert(1, "ff")
        last_mac.insert(2, "01")
        mac_list.append(last_mac)
        #print(mac_list)
    return mac_list


def generate_initiation_mac(mac_list: list, channel: str):
    """
    Generate an Initialisation_Mac with the number of send packages to enable the receiver to determine to number
    of incoming packages
    :param mac_list: return list from create_mac_list function
    :return: Initialisation Mac Address with number of packages as data
    """
    length = str(len(mac_list))
    while len(length) < 6:
        length = '0'+length
    length = ':'.join(length[i:i+2] for i in range(0, len(length), 2))
    init_mac = channel+":ff:00:"+length
    return init_mac


def mac_list_to_str_list(hex_list: list, channel: str):
    """
    Convert the list out of lists to a list out of string with the mac-addresses as data
    :param hex_list: the input list from encoding output
    :return: mac-list in string format
    """
    mac_list = create_mac_list(hex_list, channel)
    str_list = []
    for i in range(len(mac_list)):
        str_list.append(':'.join(mac_list[i]))
#   str_list.insert(0, generate_initiation_mac(mac_list))
    #print(str_list)
    return str_list


class ARPSender:

    def __init__(self, client_ip: str, sender_id: str, message: str, log: logging.Logger = logging.getLogger('arp_sender')):
        self.log = log
        self.client_ip = client_ip
        self.message = message
        self.sender_id = sender_id

    def send_arp(self):
        channel = "0"+hex(int(self.sender_id)).lstrip("0x") if int(self.sender_id) < 16 else hex(int(self.sender_id)).lstrip("0x")

        mac_list = mac_list_to_str_list(encode_decode.str_to_hex_list(encrypt_decrypt.encrypt(self.message)[0]), channel)
        init_mac = generate_initiation_mac(mac_list, channel)
        mac_list.insert(0, init_mac)
        package_count = 0
        for mac in mac_list:
            print("Sending: "+mac)
            ans, unans = srp(Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
                             ARP(pdst=self.client_ip), timeout=1)
            package_count += 1
            for snd, rcv in ans:
                self.log.info(rcv)
        print("Packages: ", package_count)

    def run(self):
        self.log.info("Transmission complete!")


def call_sender(client_ip: str, sender_id: str, message: str):

    logger = logging.getLogger()
    server = ARPSender(client_ip=client_ip, sender_id=sender_id, message=message, log=logger)
    server.send_arp()
    server.run()
