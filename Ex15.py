# Leia o ano de nascimento de uma pessoa
# Apresente uma linha do tempo de cada ano com a idade até o ano atual
nome = input('Digite seu nome: ')
nascimento = int(input('Digite seu ano de nascimento:'))
anoatual = 2025
idade = 0
while (nascimento<=anoatual):
    print(nome, ' tem ',idade, ' no ano de', nascimento, '.' )
    idade = idade +1
    nascimento = nascimento+1