# Armazene dois valores de notas de 20 alunos
# Calcule a média entre as notas
# Imprima a média de cada aluno
for _ in range(3):
    nome = input('Nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media_aluno= (nota1+nota2)/2
    if media_aluno<=10:
        print('A média do(a) aluno(a) foi: ', media_aluno)