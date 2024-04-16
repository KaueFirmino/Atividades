# -*- coding: utf-8 -*-
"""Classes e Objetos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1olZUnXH1ar6WpXKdZaMyLXKwoI67wBu6

1 - Crie uma classe que modele um quadrado:

 - Atributos: Tamanho do lado
 - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

"""2 - Crie uma classe que modele um retangulo:

 - Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
 - Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
 - Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

"""

class Retangulo:
  def __init__ (self, LadoA, LadoB):
    self.LadoA = LadoA
    self.LadoB = LadoB
  def MudarLados (self, NovoLado):
    self.LadoA = NovoLado
    self.LadoB = NovoLado
  def RetornarLados (self):
    return self.LadoA
  def CalcularArea (self):
    return self.LadoA ** 2
  def CalcularPerimetro (self):
    return self.LadoA * 4
local = Retangulo (int(input("Insira um dos lados do local: ")), int(input("Agora, outro: ")))
print (f"Serão necessários {local.CalcularArea()} rejuntes e {local.CalcularPerimetro()} rejuntes.")

"""3 - Crie uma classe que modele uma pessoa:

 - Atributos: nome, idade, peso e altura
 - Métodos: Envelhecer, engordar, emagrecer, crescer.

 Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
  def __init__(self, nome):
    self.nome = nome
  def __init__(self, idade, anos = 1):
    self.idade += anos
    if self.idade < 21
     self.idade(0,5 * anos)
  def __init__(self, peso):
    if self.peso += peso
  def __init__(self, peso):
    if self.peso -= peso
  def __init__(self, altura):
    self.altura += altura

  envelhecer = Pessoa (print(f'Você está um ano mais velho! {self.idade}'))
  engordar = Pessoa (print(f'Você engordou! {self.peso}'))
  emagrecer = Pessoa (print(f''))

"""4 - Crie uma classe para implementar uma conta corrente.

 - A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
 - Os métodos são os seguintes: alterarNome, depósito e saque;
 - No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

class con:
  sal = 0
  def __init__(self, num, nom):
    self.num = num
    self.nom = nom
  def alt_nom(self, nov_nom):
    self.nom = nov_nom
  def dep(self, dep):
    self.sal += dep
  def saq(self, saq):
    self.sal -= saq
exe_con = con(1, "Exemplo")
print(exe_con.sal)
exe_con.dep(100)
print(exe_con.sal)
exe_con.saq(50)
print(exe_con.sal)

""" 5 - Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class Televisor:
  Canal = 10
  Volume = 10
  def InformarCanal(self):
    print(self.Canal)
  def AumentarVolume(self, num):
    Volume += num
  def DiminuirVolume(self, num):
    Volume -= num
TV = Televisor()
TV.InformarCanal()
