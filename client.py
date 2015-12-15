import socket

host = '127.0.0.1'
port = 8885

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host, port))
client.send('test')
response = client.recv(1024)
client.close()
# while True:
# 	data = raw_input('>')
# 	if not data:
# 		break
# 	client.send(data)
# 	response = client.recv(4096)

# 	if not response:
# 		break
# 	print response

# client.close()