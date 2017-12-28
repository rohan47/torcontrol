#!/usr/bin/python2
from stem import Signal
from stem.control import Controller
import getpass
import socks
import socket
import requests

try:
    with Controller.from_port(port = 9051) as controller:
        password = getpass.getpass("Password:")
        controller.authenticate(password)
        controller.signal(Signal.NEWNYM)
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
        socket.socket = socks.socksocket
        r = requests.get("http://checkip.amazonaws.com/")
        print r.content.strip()
        
except Exception, e :
    print e
