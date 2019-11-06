from constantes import *
from socket import *
from paquete import *
from network import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM) 
	return UDPsocket


def rdt_send():
    data=input('ingrese un mensaje:  ')
    return(data.encode('utf-8'))


def make_pkt(data):
    paquete= Paquete(EMISOR_PORT , RECEPTOR_PORT, data, 0)
    cksum = calcular_checksum(paquete)
    paquete.set_checksum(cksum)
    return paquete  
	

def udp_send(socket, mensaje, receiver): 
	mensaje=dumps((receiver, mensaje)) 
	socket.sendto(mensaje, (NETWORK_IP,NETWORK_PORT))



def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":

	cliente=create_socket() # Creamos el socket
	
	signal.signal(signal.SIGINT, partial(close_socket, cliente))#esta funcion toma el socketal final
    
	while True: # Iteramos indefinidamente
		data=rdt_send() # Leemos el mensaje desde teclado
		paquete=make_pkt(data) # Hacemos el paquete
		destinatario = (RECEPTOR_IP, RECEPTOR_PORT) #define el destino en el que deberia llegar el packet
		udp_send(cliente, paquete, destinatario) # Enviamos a la capa red
	close_socket(cliente)  