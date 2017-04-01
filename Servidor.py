from socket import *
import threading
import pickle

meuHost = ''
minhaPorta = 6439

listaCOnexoes = []

class conexaoTCP(threading.Thread):

    #id: número de identificacao do cliente
    def __init__(self,id,com,IPCliente):
        threading.Thread.__init__(self)
        self.id = id
        self.com = com
        self.IPCliente = IPCliente
        print ('conectado com o cliente', IPCliente)
    def run(self):
        print('starting thread')
        serializado = self.com.recv(1024)
        mensagem = pickle.loads(serializado)
        tipoMensagem = mensagem[0]

        #tratamento de mensagens recebidos:
        if tipoMensagem == 1:
            tupla = [mensagem[1],mensagem[2]]
            listaCOnexoes.append(tupla)
        else :
            if tipoMensagem == 2:
                print('2')


#Criando sockets:
#add
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPorta))
sockobj.listen(5)

while True:
    print(listaCOnexoes)
    conexao, IPCliente = sockobj.accept()
    thread1 = conexaoTCP(1, conexao, IPCliente)
    thread1.start()

sockobj.close
