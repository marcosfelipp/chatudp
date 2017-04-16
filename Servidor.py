from socket import *
import threading
import pickle

meuHost = ''
minhaPorta = 6433

# Formato da lista de conexoes: ||EMAIL|IP|PORTA||

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
                contato=self.getCOntato(mensagem[1])
                if contato is None:
                    mensagem = [4]
                    serialize = pickle.dumps(mensagem)
                    sockobj.send(serialize)
                else:
                    mensagem = [3,contato[0],contato[1],contato[2]]
                    serialize = pickle.dumps(mensagem)
                    sockobj.send(serialize)

    def getCOntato(self,email):
        # buscar contato na lista de conexoes
        for contato in listaCOnexoes:
            if contato[0] == email
                return contato
        return None

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
