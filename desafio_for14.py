# Escreva um algoritmo que leia 20 números do usuário
countpar=0
for i in range(20):
   numero = int(input('Digite um número.'))
   # e exiba quantos números são pares, usando FOR. 
   if (numero%2==0):
    countpar = countpar+1
print('A quantidade de números pares é:', countpar)