#!/usr/bin/env python3
# DHCP
# Network Programming HW1
# 2015-04 T.H.Liu

import argparse, socket
import struct
from uuid import getnode as get_mac
from random import randint
port_server=67
port_client=68
MAX_BYTES = 65535

class DHCP_Discover:
    def __init__(self):
        self.transactionID = b''
        for i in range(4):
            t = randint(0, 255)
            self.transactionID += struct.pack('!B', t)

    def buildPacket(self):
        #macb = getMacInBytes()
        packet = b''
        packet += b'\x01'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0
        packet += self.transactionID       #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Your (client) IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Next server IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
        packet += b'\x00\x26\x9e\x04\x1e\x9b'   #Client MAC address: 00:26:9e:04:1e:9b
        #packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x01'   #Option: (t=53,l=1) DHCP Message Type = DHCP Discover
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet

class DHCP_Offer:
    def __init__(self):
        self.transactionID = b''
        for i in range(4):
            t = randint(0, 255)
            self.transactionID += struct.pack('!B', t)

    def buildPacket(self):
        #macb = getMacInBytes()
        packet = b''
        packet += b'\x02'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0
        packet += self.transactionID       #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\x01\x02\x03\x04'   #Your (client) IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Next server IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
        packet += b'\x00\x26\x9e\x04\x1e\x9b'   #Client MAC address: 00:26:9e:04:1e:9b
        #packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x02'   #Option: (t=53,l=1) DHCP Message Type = DHCP Discover
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet

class DHCP_Request:
    def __init__(self):
        self.transactionID = b''
        for i in range(4):
            t = randint(0, 255)
            self.transactionID += struct.pack('!B', t)

    def buildPacket(self):
        #macb = getMacInBytes()
        packet = b''
        packet += b'\x01'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0
        packet += self.transactionID       #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Your (client) IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Next server IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
        packet += b'\x00\x26\x9e\x04\x1e\x9b'   #Client MAC address: 00:26:9e:04:1e:9b
        #packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x03'   #Option: (t=53,l=1) DHCP Message Type = DHCP Discover
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet

class DHCP_ACK:
    def __init__(self):
        self.transactionID = b''
        for i in range(4):
            t = randint(0, 255)
            self.transactionID += struct.pack('!B', t)

    def buildPacket(self):
        #macb = getMacInBytes()
        packet = b''
        packet += b'\x02'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0
        packet += self.transactionID       #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\x01\x02\x03\x04'   #Your (client) IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Next server IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
        packet += b'\x00\x26\x9e\x04\x1e\x9b'   #Client MAC address: 00:26:9e:04:1e:9b
        #packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x05'   #Option: (t=53,l=1) DHCP Message Type = DHCP Discover
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port_server))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        print('Receivce 1st request from client, data[0:1] is {}', data[0:1])
        offerPacket=DHCP_Offer()
        sock.sendto(offerPacket.buildPacket(),  ('255.255.255.255',port_client))
        break
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        print('Receivce 2nd request from client, data[0:1] is {}', data[0:1])
        offerPacket=DHCP_ACK()
        sock.sendto(offerPacket.buildPacket(),  ('255.255.255.255',port_client))
        break

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port_client))
    while True:
        DiscoverPacket=DHCP_Discover()
        sock.sendto(DiscoverPacket.buildPacket(), ('255.255.255.255', port_server))
        data, address = sock.recvfrom(MAX_BYTES)
        print('Receivce 1st response from server, data[0:1] is {}', data[0:1])
        break
    while True:
        DiscoverPacket=DHCP_Request()
        sock.sendto(DiscoverPacket.buildPacket(), ('255.255.255.255', port_server))
        data, address = sock.recvfrom(MAX_BYTES)
        print('Receivce 2st response from server, data[0:1] is {}', data[0:1])
        break

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    args = parser.parse_args()
    function = choices[args.role]
    function()
