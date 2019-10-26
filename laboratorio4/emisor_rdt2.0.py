from constantes import *
from socket import *
from paquete import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM) 
	return UDPsocket


def rdt_send():
    data=input('ingrese un mensaje:  ')
    return(data.encode('utf-8'))


def make_pkt(data):
    pkt = Paquete(EMISOR_PORT , RECEPTOR_PORT, data, 0)
    ckesum = calcular_checksum(pkt)
    pkt.set_checksum(ckesum)
    return pkt  
	


def udp_send(socket, mensaje, receiver): 
	mensaje=dumps((mensaje, receiver))
	socket.sendto(mensaje, (NETWORK_IP,NETWORK_PORT)) 



def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":

	emisor=create_socket() 
	
	signal.signal(signal.SIGINT, partial(close_socket, emisor))
    
	while True: 
		data=rdt_send() 
		paquete=make_pkt(data) 
		destinatario = (RECEPTOR_IP, RECEPTOR_PORT)
		udp_send(emisor, paquete, destinatario)
	close_socket(emisor)  
		
