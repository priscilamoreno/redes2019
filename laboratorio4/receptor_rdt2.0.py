from constantes import *
from paquete import *
from constantes import *
from network import *

def create_socket(): 
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((RECEPTOR_IP,RECEPTOR_PORT))
	return servidor


def rdt_rcv(red,datos): 
	if corrupt(paquete) == NAK:
		udp_send(datos)
	else:
           datos= socket.recv(2048) 
           emisor,paquete = loads(datos) 


	return (emisor,paquete)
	
def corrupt(pckt):
	if make_pkt(paquete) == pckt:
		return NAK
	else:
		return ACK


def make_pkt(emisor,paquete): 
	paquete = Paquete()
	resultado = calcular_checksum(paquete)
	resultado.set_checksum(resultado)
	return paquete


def udp_send(paquete,emisor):
    datos = dumps(emisor,confirmacion) 
    socket.sendto(dato,(NETWORK_IP,NETWORK_PORT)) 
    return (datos)


def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)

if __name__ == "__main__":
	servidor= create_socket()

	while True:
		paquete=rdt_rcv(servidor)
		if corrupto:
			sndpkt= make_pkt(NAK)
			udp_send(sndpkt)
		else:
			data=extract(paquete)
			deliver_data(data)		
	close_socket(servidor)