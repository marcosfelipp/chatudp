from socket import *
import pickle

minhaListaDeContatos = []

serverHost = 'localhost'


print('Digite um número de porta:')
serverPort = int(input())
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

print('----------AUTENTICAÇÂO------------')
print('Digite seu endereco de email')
email = input()
print('Digite sua senha')
senha = input()


#Autenticação com servidor:
# id -> número da porta
id = sockobj.getsockname()
print(id)
mensagem = [1, email, senha,id]
serialize = pickle.dumps(mensagem)
sockobj.send(serialize)

while True:
    print('-------------MENSAGEM---------------')
    print("Digite 1 para conectar com um cliente da sua lista de contatos\nDigite 2 para solicitar um contato")
    selecao = int(input())
    if selecao == 1:
        print('Sua lista de contatos:')
        print(minhaListaDeContatos)
        print('Digite o numero contato que queira conectar')
        n = int(input())


    else:
        # buscar nos contatos e mail do cliente
        # Fazer conexao UDP com cliente
        if selecao == 2:
            # Busca no servidor:
            print('Digite um e mail para buscar no servidor')
<<<<<<< HEAD
            n = int(input())
            mensagem = [2, email]
            serialize = pickle.dumps(mensagem)
            sockobj.send(serialize)
=======
            contato = int(input())
            mensagem = [2,contato]
            serialize = pickle.dumps(mensagem)
            sockobj.send(serialize)

            # Mensagem recebida do servidor:

            serializado = sockobj.recv(1024)
            mensagem = pickle.loads(serializado)

            # Formato da mensagem recebida:
            # ||NUM_SEQUENCIA|EMAIL|IP|PORTA||

            if mensagem[1] != 3:
                print("E-mail não encontrado no servidor")
                continue
            else :
                minhaListaDeContatos.append(mensagem)

            #Conexao com o cliente:
>>>>>>> 2.0
