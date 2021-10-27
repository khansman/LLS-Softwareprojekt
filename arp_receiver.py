from scapy.layers.l2 import ARP
import sys
import logging
import socket
from scapy.sendrecv import sniff
import encode_decode
import encrypt_decrypt
import socketio

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def package_src_to_list(macs: list, s_ip: str):
    message = ""
    for i in range(len(macs)):
        mac = list(macs[i].split(":"))
        if mac.count("00") > 0:
            mac.remove("00")
        message += encode_decode.decode_message(mac)
    decrypted_message = encrypt_decrypt.decrypt(message)
    print('Message:' + decrypted_message)

    socket_endpoint = 'http://127.0.0.1:5000'
    sio = socketio.Client()
    sio.connect(socket_endpoint, transports='websocket')
    sio.emit('arp_receiver_message', {'sender_ip': s_ip, 'message': decrypted_message})


package_count = 0
rec_package_count = 0
sender_ip = 0
channel_id = 0
original_id = 0
mac_list = []


# noinspection PyGlobalUndefined
class ARPReceiver:

    def __init__(self, log: logging.Logger = logging.getLogger('arp_receiver')):
        self.log = log
        print("ARP Receiver in Progress!")

        def arp_monitor_callback(pkt):
            global original_sip
            global package_count
            global rec_package_count
            global sender_ip
            global channel_id
            global mac_list

            if ARP in pkt and pkt[ARP].op in (1, 2):
                mac_code = pkt.src
                sender_ip = pkt.psrc
                if pkt.pdst == socket.gethostbyname(socket.gethostname()):
                    try:
                        if mac_code.replace(":", "")[2:][:4] == "ff00":
                            channel_id = mac_code[:2]
                            package_count = int(mac_code.replace(":", "")[6:])
                            rec_package_count = 0
                            original_sip = sender_ip
                            self.log.info("Message from channel " + str(int("0x" + mac_code[:2], 0)) + " - " + sender_ip
                                          + " :: " + str(int(mac_code.replace(":", "")[6:])) + " packets incoming!")

                        elif mac_code[:2] == channel_id and mac_code.replace(":", "")[2:][:4] == "ff01":
                            rec_package_count += 1
                            mac_list.append(mac_code[9:])
                            if package_count == rec_package_count:
                                package_src_to_list(mac_list, str(original_sip))
                                mac_list = []
                                package_count = 0
                                rec_package_count = 0
                                channel_id = 0
                                sender_ip = 0
                                original_sip = 0
                                self.log.info("Transmission complete! \n\r")

                    except NameError:
                        print("Unrelated Package skipped!")
                        return

        sniff(prn=arp_monitor_callback, filter="arp", store=0)

    def run(self):
        self.log.info("Stopping ARP Receiver!")


def call_receiver():
    logger = logging.getLogger()
    receiver = ARPReceiver(log=logger)
    receiver.run()


if __name__ == '__main__':
    call_receiver()
