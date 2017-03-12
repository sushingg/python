#!/usr/bin/env python3
# suShinGG
# https://github.com/sushingg/python/blob/master/work/udp_chat.py
# UDP Chat client and server on localhost

import argparse, socket, sys, time, os
from threading import Thread
from datetime import datetime

MAX_BYTES = 65535
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def server(port):
    client_list = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('='*33)
    print('UDP Chat server by suShinGG')
    print('Listening at {}'.format(sock.getsockname()))
    print('='*33)
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        name,cmd,txt = text.split(':')
        text = name+': '+txt
        if cmd == 'join':
            if (name, address not in client_list):
                client_list.append([name,address])
                print('{}|{}|Joining as {!r}'.format(datetime.now(), address, name))
                text = name + ' has joining'
                data = text.encode('utf-8')
                for idx, val in enumerate(client_list):
                    name, address = client_list[idx]
                    sock.sendto(data, address)
        elif cmd == 'send':
            print('{}|{}|[{}] Send {!r}'.format(datetime.now(),address ,name, txt))
            data = text.encode('utf-8')
            for idx, val in enumerate(client_list):
                name, address = client_list[idx]
                sock.sendto(data, address)

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Thread(target=send, args=(sock,port,)).start()
    Thread(target=recv, args=(sock,port,)).start()

def send(sock,port):
    print('='*27)
    print('UDP Chat client by suShinGG')
    print('='*27)
    name = input('your name: ')
    for x in range (0,5):#forfun
        b = "Loading" + "." * x
        print (b, end="\r")
        time.sleep(0.3)
    text = name+":join:hello"
    data = text.encode('utf-8')
    sock.sendto(data, ('127.0.0.1', port))
    while True:
        text = input()
        print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
        textz = name+":send:"+text
        data = textz.encode('utf-8')
        sock.sendto(data, ('127.0.0.1', port))


def recv(sock,port):
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        print(text)

if __name__ == '__main__':
        choices = {'client': client, 'server': server}
        parser = argparse.ArgumentParser(description='UDP chat server/client By suShinGG')
        parser.add_argument('role', choices=choices, help='which role to play')
        parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                            help='UDP port (default 1060)')
        args = parser.parse_args()
        function = choices[args.role]
        function(args.p)
