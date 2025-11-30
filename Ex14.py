# Escreva um algoritmo que leia 20 números do usuário
i=1
countpar=0
while (i<=20):
    numero = int(input('Digite um número.'))
    # e exiba quantos números são pares
    if (numero%2 ==0):
        countpar=countpar+1  
    i = i+1
print(countpar)