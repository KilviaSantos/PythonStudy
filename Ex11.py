# Algoritmo que leia 10 números do usuário
# Depois calcule a soma dos número recebidos, use while
usuario = 20
soma=0
while (usuario>=1):
    num = float(input('Digite um número:'))
    soma=soma+num
    usuario=usuario-1
print('A soma dos números digitados é: ',soma)
