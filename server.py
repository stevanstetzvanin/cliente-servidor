import socket
import sys


HOST = 'localhost'   # Usa o IP da máquina
PORT = 8888 # Uma porta qualquer, desde que não esteja em uso

#Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Liga o socket ao IP e porta determinados
s.bind((HOST, PORT))

#Socket fica escutando a porta especificada
s.listen(10)
estoque = 0

print("SERVIDOR INICIADO")

conn, addr = s.accept()                                 #Fica esperando o cliente conectar
print ("Conectado a " + addr[0])

while 1:
    print ("Aguardando... ")
    data = conn.recv(1024)                                  #recebe informação
    data_decodificado = data.decode('ascii')                #decodifica em string
    if data_decodificado.lower() == "parar":
        conn.sendall("Server finalizado".encode())
        break
    elif data_decodificado.lower() == 'fim':
        print("Cliente desconectado.")
        conn, addr = s.accept()
        print ("Conectado a " + addr[0])
    elif data_decodificado[:1] == '+':
        estoque += int(data_decodificado[1:])
        print ("O cliente adicionou {} itens ao estoque. Estoque atual {} itens" .format(data_decodificado[1:],estoque))
        conn.sendall("Estoque atualizado. Estoque atual: {} itens".format(estoque).encode())  
    elif data_decodificado[:1] == '-':
        estoque -= int(data_decodificado[1:])
        print ("O cliente removeu {} itens ao estoque. Estoque atual {} itens" .format(data_decodificado[1:],estoque))
        conn.sendall("Estoque atualizado. Estoque atual: {} itens".format(estoque).encode())
    else:
        conn.sendall("Erro não foi possível atualizar o estoque.".encode())
print ("Cliente mandou, server finalizou")
s.close()