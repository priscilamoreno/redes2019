from paquete import *
from constantes import *
from network import *
from socket import *

def create_socket():
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((RECEPTOR_IP,RECEPTOR_PORT))
	return servidor

def extract(paquete): 
    data= paquete.get_datos() 
    return data

def deliver_data(message): 
	print(message)

def rdt_rcv(socket): 
	data = socket.recv(2048) 
	emisor,paquete = loads(data) 
	return (emisor,paquete)
	

def corrupto(paquete):
	if calcular_checksum(paquete) == 0:
		return True
	else:
		return False


def make_pkt(data): 
	paquete = Paquete(RECEPTOR_PORT , EMISOR_PORT, data,0)
	resultado = calcular_checksum(paquete)  
	paquete.set_checksum(resultado)
	return paquete


def udt_send(socket,emisor,paquete): 
	datos = dumps((emisor,paquete)) 
	socket.sendto(datos,(NETWORK_IP,NETWORK_PORT))
	return (datos)


def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)

if __name__ == "__main__":
	servidor= create_socket()# Creamos el socket "receiver"
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, servidor))
	print ("listo para recibir mensajes..")# Imprimimos el cartel "Listo para recibir mensajes..."

	secuencia=0
	while True:
		emisor, paquete=rdt_rcv(servidor)
		print (emisor,paquete)
		if corrupto(paquete) ==0: 
			emisor = (EMISOR_IP,EMISOR_PORT)
			pkt = make_pkt("NAK") 
			udt_send(servidor,emisor,pkt) 
		else: 
			emisor = (EMISOR_IP,EMISOR_PORT) 
			pkt2 = make_pkt("ACK")
			data= extract(paquete)# Extrae los datos
			deliver_data(data)# Entregamos los datos a la capa de aplicacion
			udt_send(servidor,emisor,pkt2) #los envia a la red y al emisor
			secuencia = (secuencia + 1) // 2 
	close_socket(servidor)