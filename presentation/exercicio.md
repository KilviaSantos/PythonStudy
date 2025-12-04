---
marp: true
theme: default
paginate: true
style: |
  pre, code {
    font-size: 1.2em; /* Increase code font size */
  }
---


# Encontre o mais novo

> Desenvolva um algoritmo que leia o nome e a idade de 5 pessoas e imprima o nome e idade da pessoa mais nova.


_A cada novo passo, faça um **commit** e envie seu codigo para o github_

---

# Encontre o mais novo

## Passo 1: 

> Escreva um loop que execute 10 vezes

---

# Encontre o mais novo

## [REPOSTA] Passo 1: 

> Escreva um loop que execute um print('ola') 10 vezes


``` python

for i in range(10):
  print('ola')

```

---

# Encontre o mais novo

## Passo 2: 

> A cada iteração, pergunte ao usuário o nome e idade

---

# Encontre o mais novo

## [RESPOSTA] Passo 2: 

> A cada iteração, pergunte ao usuário o nome e idade

``` python

for i in range(10):
  nome = input('Digite seu nome: ')
  idade = int(input('Digite sua idade: '))

```

---

## Passo 3: 

> O objetivo do algoritmo é encontrar e imprimir o mais novo. Mas não é possivel imprimir o nome e idade depois do loop

``` python {5-6}
for i in range(10):
  nome = input('Digite seu nome: ')
  idade = int(input('Digite sua idade: '))

print(nome) # bug: apenas o ultimo nome será impresso 
print(idade) # bug: apenas a ultimo idade será impressa
```


---

## [RESOLUÇÃO] Passo 3: 

> É importante que criemos 2 novas variaveis

```python {1-2,8-9}
nome_mais_novo = ""
idade_mais_novo = 0;

for i in range(10):
  nome = input('Digite seu nome: ')
  idade = int(input('Digite sua idade: '))

print(nome_mais_novo)  
print(idade_mais_novo) 
```

---

## [RESOLUÇÃO] Passo 3: 

> Agora podemos sempre comparar a idade que o usuário digitou com que a temos armazenado!


```python {7-8}
nome_mais_novo = ""
idade_mais_novo = 0;
for i in range(10):
  nome = input('Digite seu nome: ')
  idade = int(input('Digite sua idade: '))
  if ( False """ CONDICAO ? """ ):
    nome_mais_novo = nome
    idade_mais_novo = idade
print(nome_mais_novo)  
print(idade_mais_novo) 
```

---

> Mas qual a condição para isso?

```python {6}
nome_mais_novo = ""
idade_mais_novo = 0
for i in range(10):
  nome = input('Digite seu nome: ')
  idade = int(input('Digite sua idade: '))
  if ( i == 0 or idade < idade_mais_novo ):
    nome_mais_novo = nome
    idade_mais_novo = idade
print(nome_mais_novo)  
print(idade_mais_novo) 
```
