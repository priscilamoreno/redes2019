from constantes import *
from paquete import *
from network import *

def create_socket():
    UDPsocket=socket(AF_INET, SOCK_DGRAM)
    UDPsocket.bind((RECEPTOR_IP, RECEPTOR_PORT)) 
    return UDPsocket

def extract(packet): 
    data=packet.get_data()
    return data

def deliver_data(message):
    print(message)

def rdt_recv(socket):
    datos=socket.recvfrom(2048) 
    emisor, paquete=loads(datos) 
    '''print(paquete)'''
    return emisor, paquete

def make_pkt(datos):
    paquete=Paquete(receptor, emisor, datos, 0)
    ckecksum=calcular_checksum(paquete)
    paquete.set_checksum(ckecksum)
    return paquete

def corrupto(paquete):
    if paquete.set_checksum()== 0:
        return True
    else:
        return False

def udp_send(paquete, emisor): 
    datos=dumps(emisor, confirmacion) 
    socket.sento(datos, (NETWORK_IP, NETWORK_PORT))
    return datos

def close_socket(socket, signal, frame):
    print ("\rCerrando socket")
    socket.close()
    exit(0)


if __name__ == "__main__":
    servidor=create_socket()
    # Creamos el socket "receiver"

    # Registramos la senial de salida
    signal.signal(signal.SIGINT, partial(close_socket, servidor))
    # Imprimimos el cartel "Listo para recibir mensajes..."
    print("Listo para recibir mensajes...")

    # Iteramos indefinidamente
    while True:
                secuencia=0
                #num de id del paquete
                recv_paquete=rdt_recv(servidor)#servidor
                #Recibimos un paquete de la red
                addr, msg=rdt_recv(servidor)

                print("rec msg %s: %s" % (addr, msg))
                if recv_paquete and corrupto:
                    sndpkt=make_pkt("NAK")
                    paquete=rdt_recv(servidor)
                elif recv_paquete and not corrupto:
                    data=extract(paquete)
                    #Extraemos los datos
                    deliver_data(data)
                    #Entregamos los datos a la cap de aplicacion
                    paquete=make_pkt("ACK",checksum)
                    udt_send(paquete)
    close_socket()