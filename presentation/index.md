---
marp: true
theme: default
paginate: true
---

# Introdução ao Python

Python é uma linguagem de programação de alto nível, fácil de aprender e muito utilizada em ciência de dados, web, automação e muito mais.

---

# Primeiros Passos

- Sintaxe simples e legível
- Não precisa de ponto e vírgula no final das linhas
- Indentação é obrigatória para blocos de código

<br>

```python
print("Olá, mundo!")
```

---

# Cuidado com os bugs

> Bugs são uma parte natural do processo de codificar. Eles são problemas que você deve resolver. E isso faz parte do processo de se tornar um otimo programador.


---

# Cuidado com os bugs

``` python
# esquecer de fechar o parentese `)`
print("hello, world" 

# ou acrescentar mais aspas do que o necesssario
print("hello "")  
```

``` python
# ou esquecer de colocar a virgula necessaria
print("ola " nome, ". Bom dia")

# ou esquecer o tab da estrutura de decição ou de repetição
if (idade > 18):
print("É maior de idade")
```

--- 

# Corrigindo BUGS

``` python {2,6}
#print("hello, world" 
print("hello, world") 

# ou acrescentar mais aspas do que o necesssario
#print("hello "")  
print("hello ")  
```

---

# Corrigindo BUGS

```python {3,9-10}
# ou esquecer de colocar a virgula necessaria
print("ola " nome, ". Bom dia")
print("ola ", nome, ". Bom dia")

# ou esquecer o tab da estrutura de decição ou de repetição
if (idade > 18):
print("É maior de idade")

if (idade > 18):
  print("É maior de idade")
```


---

# Variáveis e Tipos de Dados

- Não é necessário declarar o tipo
- Tipos comuns: int, float, str, bool

```python
idade = 20      # inteiro
altura = 1.75   # float
nome = "Ana"    # string
ativo = True    # booleano
```

---

# Entrada e Saída

Para ler dados do usuário e exibir na tela:

```python
nome = input("Qual seu nome? ")
print(f"Bem-vindo, {nome}!")
```

---

# Operadores

- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparação: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `and`, `or`, `not`

```python
resultado = (5 + 3) * 2
print(resultado)
```

---

# Condicionais

Permitem executar blocos de código dependendo de condições.

```python {2, 4}
idade = 18
if idade >= 18:
  print("Maior de idade")
elif idade >= 16:
  print("Menor de idade que pode votar")
else:
  print("Menor de idade")
```

---

![bg left:33%](http://localhost:9090/800x600/000/fff/?text=while)
![bg left:33% vertical](http://localhost:9090/800x600/000/fff/?text=for)


```python
contador = 0 # controlador do loop
while contador < 5: # condicao
  print(contador)
  contador += 1 # incremento 
```

<br>

<br>

```python
 # Já não é mais necessário definir 
 # variavel, condicação e incremento 
 # para controlar o loop

for contador in range(5):
  print(contador)
```

---

# Boas Práticas

- Use nomes de variáveis descritivos
- Comente seu código
- Siga a indentação padrão (tab)
- Teste sempre seu código

---

# Fim

Obrigado! Perguntas?
