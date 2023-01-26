import socket 
 def farenheit_to_celcius(farenheit):  	celcius = (farenheit - 32)* 5/9 
 	return celcius 
 def main(): 
 	host = '' 
 	port = 7878 
 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  	s.bind((host, port)) 
 	s.listen(1) 
 	print(f'Listening on {host}:{port}')  	conn, addr = s.accept()  	print(f'Connection is from {addr}')  	while True: 
 	 	data = conn.recv(1024).decode()  	 	if not data:  	 	    break 
 	 	print(f'Received {data}')  	 	farenheit = float(data) 
 	 	celcius = farenheit_to_celcius(farenheit) 
 	 	celcius = round(celcius, 2)  	 	conn.sendall(str(celcius).encode()) 
 	conn.close() 
 if __name__ == '__main__':  	main() 
