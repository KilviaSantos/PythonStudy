#Leia 20 números do usuário
#exiba quantos são maiores que 8.
usuario = 20
maior8 = 0
while (usuario>=1):
    numero = int(input('Digite um número: '))
    if (numero>8):
        maior8 = maior8 + 1
    usuario = usuario - 1
print('Existem',maior8, 'números maiores que 8.')