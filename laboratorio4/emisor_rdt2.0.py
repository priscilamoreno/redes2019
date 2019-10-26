from constantes import *
from socket import *
from paquete import *

def create_socket():
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
    return UDPsocket

def rdt_send():
    sndpkt = input('ingrese el mensaje: ' )
    return (sndpkt.encode('utf-8'))

def make_pkt(sndpkt):
    pckt = Paquete(RECEPTOR_PORT, RECEPTOR_PORT, sndpkt, 0)
    check = calcular_checksum(pckt)
    pckt.set_checksum(check)
    return pckt

def udp_send(socket, pckt, receptor):
    data= dumps((pckt, receptor)) 
    socket.sendto(data, (NETWORK_IP, NETWORK_PORT))

def rdt_rcv(socket): 
    data=socket.recvfrom(2048)
    receptor, paquete=loads(data) 
    '''print(paquete)'''
    return emisor, paquete  

def close_socket(socket, signal, frame):
    print("\n\rCerrando socket")
    socket.close()
    exit(0)

if __name__ == '__main__':
    cliente = create_socket()
    
    signal.signal(signal.SIGINT, partial(close_socket, cliente))

    while True:
        secuencia=0
        data=rdt_send() 
        rcv_paquete = rdt_rcv(cliente)
        paquete=make_pkt(data)
        destinatario=(RECEPTOR_IP, RECEPTOR_PORT) 
        udp_send(cliente, destinatario, paquete) 
        if rdt_rcv () and corrupto(paquete) is Ack(rcv_paquete,1):
            udt_send(paquete)
        if red_rcv () and not corrupto and  Ack(recv_paquete,0):
            secuencia = (secuencia + 1) // 2

    close_socket(cliente)