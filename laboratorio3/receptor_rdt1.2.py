from constants import *
from pickle import *
from socket import *

def create_socket(address, port):
    # IMPLEMENTAR
    UDPsocket=socket(AF_INET, SOCK_DGRAM)
    UDPsocket.bind((address, port))
    return UDPsocket

#def print_message(message):
    #print (message)

def extract(packet):
    # IMPLEMENTAR
    datas = packet.get_data()
    #return datas
    print(datas)

def rdt_rcv(sock):
    # IMPLEMENTAR
    packet = loads(sock.recv(2048))
    return packet

def deliver_data(datas):
    # IMPLEMENTAR
    return datas

def close_socket(socket, signal, frame):
    print ("\rCerrando socket")
    socket.close()
    exit(0)


if __name__ == "__main__":
    # Creamos el socket "receiver"
    receptor = create_socket(RECEIVER_IP, RECEIVER_PORT)
    # Registramos la senial de salida
    signal.signal(signal.SIGINT, partial(close_socket, receptor))
    # Imprimimos el cartel "Listo para recibir mensajes..."
    print('receptor corriendo')
    # Iteramos indefinidamente
    while True:
        # Recibimos un paquete de la red
        packet = rdt_rcv(receptor)
        # Extraemos los datos
        datas = extract(packet)
        # Entregamos los datos a la capa de aplicacion
        deliver_data(datas)#4
        archivo = open('DATA.txt', 'a') # a: anexa
        archivo.write(str(datas)+'\n')
        archivo.close()
close_socket(receptor)