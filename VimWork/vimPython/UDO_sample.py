# coding=utf-8
import argparse, socket
from datetime import datetime

MAX_BYTES = 65535


def server(port):
    sock = socket.socket(socket.AF_INET, socket.Sock_DGRAM)
    sock.bind(('127.0.0.1'), port)
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client an {} asys {!r}'.format(address, text))
        text = "Your data was {} bytes long".format(len(date))
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.endocde('ascii')
    sock.sento('127.0.0.1', port)
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES
