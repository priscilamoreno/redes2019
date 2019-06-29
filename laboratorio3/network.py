from socket import *
from pickle import *
from constants import *
from packet import *

def recv_pckt(socket):
	data, address = socket.recvfrom(1024)
	receiver, pckt = loads(data)
	return receiver, pckt

def send_pckt(socket, receiver, pckt):
	data = dumps(pckt)
	socket.sendto(data, receiver)

def process_pkt(pckt):
	addrs = (pckt)
	return pckt, addrs

def shut_down(socket, signal, frame):
	print ("\rCerrando red...")
	socket.close()
	print ("...Red cerrada")
	exit(0)

if __name__ == "__main__":
	# Creamos el socket para la red
	sock = socket(AF_INET, SOCK_DGRAM)
	# Lo ligamos a su direccion
	sock.bind((NETWORK_IP, NETWORK_PORT))
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(shut_down, sock))
	# Imprimimos mensaje
	print('Red Habilitada')
	while True:
		receiver, pckt = recv_pckt(sock)
		send_pckt(sock, receiver, pckt)

