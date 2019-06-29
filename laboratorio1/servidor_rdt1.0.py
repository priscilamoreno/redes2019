from socket import*

def create_UDPsocket(address,port):
   UDPsocket= socket(AF_INET, SOCK_DGRAM)
   UDPsocket.bind((address, port))
   return UDPsocket

def rdt_rcv(socket):
  packet=socket.recv(2048)
  return packet

def extract(packet):
 return packet.decode('utf-8')

def deliver_data(data):
 print(data.upper())
 return data

def close_socket(socket):
   socket.close()

if __name__ == "__main__":
   servidor=create_UDPsocket('localhost',20000)
   print('servidor corriendo')
   while True:
      packet=rdt_rcv(servidor)
      data=extract(packet)
      deliver_data(data)
   close_socket(servidor)
