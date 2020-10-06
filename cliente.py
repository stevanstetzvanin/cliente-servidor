import socket

print("CLIENTE INICIADO")

host = 'localhost'
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria o socket
s.connect((host, port))                               #conecta ao servidor

while True:
    inserir = input("\nUtilize o prefixo + ou - e digite a quantidade para adicionar ou remover itens ao estoque.\nEnvie FIM para fechar o cliente e PARAR para finalizar o servidor: ")
    s.send(inserir.encode())
    if (inserir.lower() == 'fim' or inserir.lower() == 'parar'):
        print("Cliente finalizado.")
        break
    reply = s.recv(1096)                                  #recebe a resposta
    print ("O servidor respondeu: ", reply.decode())

s.close()                                             #Fecha a conexão
