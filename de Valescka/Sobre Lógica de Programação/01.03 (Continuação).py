# -*- coding: utf-8 -*-
"""Atividade (continuação).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZfF65yR_gvsG-vd8GHP8O3B5BxndUsV1
"""

# Faça um programa que peça um valor e mostre se ele é positvo ou negativo.

a = int(input("Insira um valor: "))

if a > 0:
    print("O valor inserido é positivo.")
elif a < 0:
    print("O valor inserido é negativo.")
else:
    print("O valor inserido é zero.")

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

a = input("Insira F (feminino) ou M (masculino): ")

if a == 'F':
    print("Você inseriu F (feminino).")
elif a == 'M':
    print("Você inseriu M (masculino).")
else:
    print("Sexo inválido.")

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['a', 'e', 'i', 'o', 'u']
a = input("Insira uma letra: ")

if a in vogais:
    print("A letra inserida é uma vogal.")
else:
    print("A letra inserida é uma consoante.")

# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno apresentar: [...]

a = 0

for i in range(2):
    a = a + float(input(f"Insira a {i + 1}ºa nota parcial: "))

if a > 7:
    print("Aprovado.")
elif a < 7:
    print("Reprovado.")
elif a == 10:
    print("Aprovado com distinção.")

# Faça um Programa que leia três números e mostre o maior deles.

a = []

for i in range(3):
    a.append(int(input("Insira um número: ")))

print(f"O maior número entre os inseridos é {max(a)}.")

# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = []

for i in range(3):
    a.append(int(input("Insira um número: ")))

print(f"O menor número entre os inseridos é {min(a)}.")

#  Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

a = 0
b = 0

for i in range(3):
    b = float(input(f"Insira o preço do produto {i + 1}: "))
    if b < a:
        a = i

print(f"Você deve comprar o {i}ºo produto.")

# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = []

for i in range(3):
    a.append(int(input("Insira um número: ")))

a.sort(reverse=True)

print(a)

# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: [...]

salario = float(input("Insira o seu salário: "))

if salario < 280:
    print(f"Você ganha, atualmente, R$ {salario}; com um percentual de aumento de R$ {salario * 0.20} aplicado, agora você ganha R$ {salario + salario * 0.20}.")
elif salario > 280 and salario < 700:
    print(f"Você ganha, atualmente, R$ {salario}; com um percentual de aumento de R$ {salario * 0.15} aplicado, agora você ganha R$ {salario + salario * 0.15}.")
elif salario > 700 and salario < 1500:
    print(f"Você ganha, atualmente, R$ {salario}; com um percentual de aumento de R$ {salario * 0.10} aplicado, agora você ganha R$ {salario + salario * 0.10}.")
else:
    print(f"Você ganha, atualmente, R$ {salario}; com um percentual de aumento de R$ {salario * 0.05} aplicado, agora você ganha R$ {salario + salario * 0.05}.")

# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas: [...]

def podeSerTriangulo(ladoA, ladoB, ladoC):
    if ladoA + ladoB > ladoC:
        return 1

def qualTriangulo(ladoA, ladoB, ladoC):
    if ladoA == ladoB and ladoB == ladoC:
        return 1
    elif (ladoA == ladoB and ladoB != ladoC) or (ladoA == ladoC and ladoC != ladoB) or (ladoB == ladoC and ladoC != ladoA):
        return 2
    else:
        return 3;

a = float(int("Insira o primeiro lado do triângulo: "))
b = float(int("Insira o segundo lado do triângulo: "))
c = float(int("Insira o terceiro lado do triângulo: "))

if podeSerTriangulo(a, b, c):
