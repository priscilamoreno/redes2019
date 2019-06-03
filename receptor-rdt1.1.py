# redes2019
from socket import *
from paquete import *
from constantes import *
from pickle import *

def create_UDPsocket(address, port):
    UDPsocket=socket(AF_INET, SOCK_DGRAM)
    UDPsocket.bind((address, port))
    return UDPsocket
def deliver_data(data):
    print (data)
def rdt_rcv(socket):
    packet = loads(socket.recv(2048))
    return packet
def extract(packet):
    data = packet.get_data()
    return data
def close_socket(socket):
    socket.close()

if __name__ == "__main__":
    receptor= create_UDPsocket(RECEIVER_IP, RECEIVER_PORT)
    print('receptor corriendo')
    while 1:
        packet = rdt_rcv(receptor)
        data = extract(packet)
        deliver_data(data)
    close_socket(receptor)

