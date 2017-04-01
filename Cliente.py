from socket import *
import pickle

minhaListaDeContatos = []

serverHost = 'localhost'
serverPort = 6439
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

print('----------AUTENTICAÇÂO------------')
print('Digite seu endereco de email')
email = input()
print('Digite sua senha')
senha = input()

#Autenticação com servidor  :
mensagem = [1, email, senha]
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
    else :
        if selecao == 2:
            print('Digite um e mail para buscar no servidor')
            n = int(input())
