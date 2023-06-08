import socket

#Crea un objeto de socket
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Obtener el nombre de host y el numero de puerto
host = socket.gethostname()
puerto = 8002

#Vincula el servidor al host y puerto especificado
servidor.bind((host, puerto))

#Escucha las conexiones entrantes
servidor.listen(5)
print(servidor)

while True:
    #Acepta una conexion entrante 
    cliente, direccion =servidor.accept()
    print("Conexion Establecida desde: ",direccion)

    #Envia mensaje de bienvenida al cliente
    mensaje = "Bienvenido al servidor"
    cliente.send(mensaje.encode('utf-8'))

    #Cierra la conexion con el cliente
    despedida = "Mensaje recibido"
    cliente.send(despedida.encode('utf-8'))
    cliente.close()