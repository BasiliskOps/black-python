import os
import paramiko 
import socket
import sys 
import threading 

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))

class Server (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind,  chanid):
        if kind == 'session':
            return paramiko.OPEEN_SUCEEDED
        return paramiko.OPEN_FAILED_ADMINSITRATIVELY_PROHIBITED


