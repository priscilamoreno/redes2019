# redes2019
from paquete import *
from constantes import *
from pickle import *
from socket import *

#EMISOR(emisor)

def create_UDPsock():
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
    return UDPsocket
def rdt_send():
    data = input('Ingrese el mensaje a enviar: ')
    return data.encode('utf-8')
def make_pkt(data):
    pkt=Packet(SOURCE_PORT,RECEIVER_PORT,data)
    return pkt
def udp_send(socket, pkt):
    dato = dumps(pkt)
    socket.sendto(dato,(RECEIVER_IP,RECEIVER_PORT))
def close_socket(socket):
    UDPsocket.close()

if __name__ == "__main__":
    emisor=create_UDPsock()
    while 1:
        data = rdt_send()
        pkt = make_pkt(data)
        udp_send(emisor, pkt)
    close_socket(emisor)

