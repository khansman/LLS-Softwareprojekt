from scapy.layers.l2 import ARP
import sys
import logging
import socket

from scapy.sendrecv import sniff

import encode_decode
import encrypt_decrypt

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def package_src_to_list(macs: list):
    message = ""
    for i in range(len(macs)):
        mac = list(macs[i].split(":"))
        if mac.count("00") > 0:
            mac.remove("00")
        message += encode_decode.decode_message(mac)
    print(encrypt_decrypt.decrypt(message))


package_count = 0
rec_package_count = 0
sender_ip = 0
channel_id = 0
mac_list = []


class ARPReceiver:

    def __init__(self, log: logging.Logger = logging.getLogger('arp_receiver')):
        self.log = log

        def arp_monitor_callback(pkt):
            global package_count
            global rec_package_count
            global sender_ip
            global channel_id
            global mac_list

            if ARP in pkt and pkt[ARP].op in (1, 2):
                mac_code = pkt.src
                sender_ip = pkt.psrc
                dst_ip = pkt.pdst

                local_ip = socket.gethostbyname(socket.gethostname())
                
                try:
                    if mac_code.replace(":", "")[2:][:4] == "ff00" and dst_ip == local_ip:
                        channel_id = mac_code[:2]
                        package_count = int(mac_code.replace(":", "")[6:])
                        rec_package_count = 0
                        print(sender_ip)
                        self.log.info("Message from channel " + str(int("0x"+mac_code[:2], 0)) + " - " + sender_ip
                                      + " :: " + str(int(mac_code.replace(":", "")[6:])) + " packets incoming!")
                    elif mac_code[:2] == channel_id:
                        rec_package_count += 1
                        mac_list.append(mac_code[3:])

                        if package_count == rec_package_count:
                            package_src_to_list(mac_list)
                            mac_list = []
                            package_count = 0
                            rec_package_count = 0
                            channel_id = 0
                            sender_ip = 0
                            self.log.info("Transmission complete! \n\r")

                except NameError:
                    print("Unrelated Package skipped!")
                    return

        sniff(prn=arp_monitor_callback, filter="arp", store=0)

    def run(self):
        self.log.info("Stopping ARP Receiver!")


if __name__ == '__main__':
    logger = logging.getLogger()
    receiver = ARPReceiver(log=logger)
    receiver.run()
