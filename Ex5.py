# Faça, usando enquanto, uma calculadora que peça dois valores do tipo real
value1 = float(input('Informe o primeiro valor:'))
value2 = float(input('Informe o segundo valor:'))

print('Menu de Opções')
print('1- Somar')
print('2- Subtrair')
print('3- Dividir')
print('4- Multiplicar')
print('5- Sair')
choice = int(input('Escolha uma opção:'))

while (choice<=4) and (choice>=1):
    
    if choice==1:
        somar= (value1+value2)
        print(somar)
        choice= choice - 6
    elif choice==2:
        subtrair= (value1-value2)
        print(subtrair)
        choice= choice - 6
    elif choice==3:
        dividir= (value1/value2)
        print(dividir)
        choice= choice - 6
    elif choice==4:
        multiplicar = (value1*value2)
        print(multiplicar)
        choice= choice - 6
    else:
        print('Fim')
# e com isso ele possa escolher se deseja somar, subtrair, dividir ou mutiplicar esses valores

#a calculadora dará uma para as quatro opções e uma quita para sair ou desligar o sistema.