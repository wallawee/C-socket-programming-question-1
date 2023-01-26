import socket 
 def main(): 
 	host = '10.0.2.15' 
 	port =  7878 
   	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  	s.connect((host, port)) 
 
 	farenheit = input("Enter a temperature  in Fahrenheit:")  	s.send(farenheit.encode('utf-8'))  
 	data  = s.recv(1024).decode('utf-8') 
 	print("Received temperature in Celsius:" + str(data)) 
 
 	s.close() 
 if __name__ == '__main__': 
    main() 
