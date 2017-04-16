from socket import *
import pickle
import threading

minhaListaDeContatos = []
serverHost = 'localhost'
serverPort = 9697

#Abre uma conexão UDP e aguarda mensagens de outros usuários:
class conexaoUDP(threading.Thread,udp):
    def __init__(self):
        threading.Thread.__init__(self)
        self.udp = udp
        print('Porta UDP aberta')
    def run(self):
        print('Esperando mensagens UDP')
        msg, cliente = self.udp.recvfrom(1024)

# Formato do contato
# ||EMAIL|IP|PORTA||
def buscaContato(email):
    for contato in minhaListaDeContatos:
        if contato[0] == email:
            return contato
    print('contato não encontrado')
    exit(1)


# Handshake
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

print('----------AUTENTICAÇÂO------------')
print('Digite seu endereco de email')
email = input()
print('Digite sua senha')
senha = input()
print('Digite um número de porta que deseja(PARA CONEXÂO UDP):')
serverPortUDP = int(input())

# Abertura do socket UDP:
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (serverHost, serverPortUDP)
udp.bind(orig)
ThreadUDP = conexaoUDP(udp)
ThreadUDP.start()


# Autenticaçao com servidor
mensagem = [1, email,serverHost,serverPortUDP]
serialize = pickle.dumps(mensagem)
sockobj.send(serialize)

while True:
    print('-------------MENSAGEM---------------')
    print("Digite 1 para conectar com um cliente da sua lista de contatos\n"
          "Digite 2 para solicitar um contato")
    selecao = int(input())
    if selecao == 1:
        print('Sua lista de contatos:')
        print(minhaListaDeContatos)
        print('Digite o email contato que queira conectar')
        email = int(input())
        contato = buscaContato(email)


    else:
        # buscar nos contatos e mail do cliente
        # Fazer conexao UDP com cliente
        if selecao == 2:
            # Busca no servidor:
            print('Digite um e mail para buscar no servidor')
            contato = int(input())
            mensagem = [2,contato]
            serialize = pickle.dumps(mensagem)
            sockobj.send(serialize)

            # Mensagem recebida do servidor:

            serializado = sockobj.recv(1024)
            mensagem = pickle.loads(serializado)

            # Formato da mensagem recebida:
            # ||NUM_SEQUENCIA|EMAIL|IP|PORTA||

            if mensagem[0] != 3:
                print("E-mail não encontrado no servidor")
                continue
            else :
                contatoRecebido = [mensagem[1],mensagem[2],mensagem[3]]
                minhaListaDeContatos.append(contatoRecebido)
                #Conexao com o cliente:


