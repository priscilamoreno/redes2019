from socket import *

def create_socket():
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
    return UDPsocket

def rdt_send():
   data=input('ingrese un mensaje: ')
   return data

# Nota: make es crear o hacer en ingles
def make_pkt(data):
  return data.encode('UTF-8')

# Nota: send es enviar en ingles.
def udp_send(socket, receiver, message):
   socket.sendto(message, receiver)

def close_socket(socket):
   socket.close()

if __name__ == "__main__":
       client=create_socket()
       while True:
            data = rdt_send()
            paquete = make_pkt(data)
            udp_send(client,('localhost',20000),paquete)
            close_socket(client)
  