from socket import *
import threading
import pickle

meuHost = ''
minhaPorta = 6433

<<<<<<< HEAD
# Formato: [email , [ip,porta] ]
=======
# Formato da lista de conexoes: ||EMAIL|IP|PORTA||
>>>>>>> 2.0
listaCOnexoes = []

class conexaoTCP(threading.Thread):

    #id: numero de identificacao do cliente --socket--
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

        # Tipos de mensagens:
        # 1: Mensagem de autenticaçao
        # 2: Mensagem de pedido de email
        if tipoMensagem == 1:
            tupla = [mensagem[1],mensagem[2],mensagem[3]]
            listaCOnexoes.append(tupla)
        else :
            if tipoMensagem == 2:
                self.getCOntato(mensagem[1])

    def getCOntato(self,email):
        #buscar contato na lista de conexões


        # Formato da mensagem a enviar:
        # ||NUM_SEQUENCIA|EMAIL|IP|PORTA||

#Criando sockets:
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPorta))
sockobj.listen(5)

while True:
    print(listaCOnexoes)
    conexao, IPCliente = sockobj.accept()
    thread1 = conexaoTCP(1, conexao, IPCliente)
    thread1.start()

sockobj.close
