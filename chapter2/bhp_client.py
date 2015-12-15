import socket


def client_sender(buffer):
	
	target = '127.0.0.1'
	port = 9999

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((target,port))

		if len(buffer):

			client.send(buffer)

		while True:
			recv_len = 1
			response = ''

			while recv_len:

				data = client.recv(4096)
				recv_len = len(data)
				response = data

				if recv_len < 4096:
					break
				print response

				buffer = raw_input("")
				buffer += '\n'

				client.send(buffer)
	except:
		print "[*] Exception! Exiting."

	client.close()




if __name__ == '__main__':
	client_sender(buffer)
	