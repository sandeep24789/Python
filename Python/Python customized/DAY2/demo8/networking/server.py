import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send(str.encode('Thank you for connecting'))
s.connect((host, port))   
print(str(c.recv(1024)))
while True:
   msg = input('Enter your name: ')
   s.send(str.encode(msg))
   


c.close()      
   
