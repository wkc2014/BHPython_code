import socket

def client_sender(buffer):
	target = '127.0.0.1'
	port = 8889
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((target,port))
		print 'Connect success!'
		# if len(buffer):
		# 	print '2'
		# 	client.send(buffer)

		while True:

			buffer = raw_input("<")
			if not buffer:
				break

			client.send(buffer)
			data = client.recv(4096)
			if not data:
				break
				
			print data

	except Exception as e:
		print "[*] Exception! Exiting."

	client.close()


if __name__ == '__main__':
	client_sender(buffer)
	

	# target = '127.0.0.1'
	# port = 8889
	# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# try:
	# 	client.connect((target,port))
	# 	print 'Connect success!'
	# 	if len(buffer):

	# 		client.send(buffer)

	# 	while True:
	# 		recv_len = 1
	# 		response = ''

	# 		while recv_len:

	# 			data = client.recv(4096)
	# 			recv_len = len(data)
	# 			response = data

	# 			if recv_len < 4096:
	# 				break
	# 			print response

	# 			buffer = raw_input("")
	# 			buffer += '\n'

	# 			client.send(buffer)
	# except Exception as e:
	# 	print "[*] Exception! Exiting."

	# client.close()