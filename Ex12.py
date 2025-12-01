# Leia o nome e a idade de 10 pessoas
# Exiba o nome e a idade da pessoa mais nova

nome_menor = ''
idade_menor = 0

for _ in range(10):
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    if (idade_menor==0) or (idade<idade_menor):
        nome_menor =nome 
        idade_menor = idade
        
print('O(a) ', nome_menor, 'tem a menor idade que é: ', idade_menor, 'anos.' )



