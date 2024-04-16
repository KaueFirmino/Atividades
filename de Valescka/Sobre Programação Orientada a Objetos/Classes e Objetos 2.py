# -*- coding: utf-8 -*-
"""Atividade 2 - classes e objetos

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u6b-WK5Yj2kWiC77pV3AbgDoLAzZxMug

1. Crie uma classe que modele uma pessoa
(a) Atributos: nome, idade e endereço
(b) Metodos: mostrar endereço e alterar endereço
"""

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print(f"Endereço de {self.nome}: {self.endereco}")

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print(f"Endereço de {self.nome} alterado para: {self.endereco}")

pessoa1 = Pessoa("Talita", 30, "Avenida Samuel Mac Dowell, 2024")
pessoa1.mostrar_endereco()

pessoa1.alterar_endereco("Rua Manuel Costa, 456")
pessoa1.mostrar_endereco()

"""2. Crie uma classe que modele uma aluno
(a) Atributos: nome, numero de matr ´ ´ıcula e curso
(b) Metodos: mostrar curso e alterar curso
"""

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        print(f"O curso de {self.nome} é {self.curso}")

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        print(f"Curso de {self.nome} alterado para {self.curso}")

# Exemplo de uso
aluno1 = Aluno("Ilana", 56984, " Pedagogia")
aluno1.mostrar_curso()

# Alterando o curso
aluno1.alterar_curso("Engenharia mecatrônica")
aluno1.mostrar_curso()

"""3. Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie metodos para acessar o nome e a m ´ edia do aluno. ´
(a) Permita ao usuario entrar com os dados de 5 alunos. ´
(b) Encontre o aluno com maior media geral. ´
(c) Encontre o aluno com menor media geral ´
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovac¸ao.
"""

class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

#entrar com os dados de 5 alunos
alunos = []
for i in range(5):
    matricula = input("Matrícula do aluno: ")
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota da primeira prova: "))
    nota2 = float(input("Nota da segunda prova: "))
    nota3 = float(input("Nota da terceira prova: "))
    aluno = Aluno(matricula, nome, nota1, nota2, nota3)
    alunos.append(aluno)

#aluno com maior média geral
aluno_maior_media = max(alunos, key=lambda x: x.calcular_media())

#aluno com menor média geral
aluno_menor_media = min(alunos, key=lambda x: x.calcular_media())

#verificar se cada aluno foi aprovado ou reprovado
for aluno in alunos:
    media = aluno.calcular_media()
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    print(f"O aluno {aluno.nome} com matrícula {aluno.matricula} obteve média {media:.2f} - {situacao}")

# Resultados
print(f"Aluno com maior média geral: {aluno_maior_media.nome} com média {aluno_maior_media.calcular_media():.2f}")
print(f"Aluno com menor média geral: {aluno_menor_media.nome} com média {aluno_menor_media.calcular_media():.2f}")

"""4. Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os
métodos para fazer as operacões de incremento (de segundos) no horário e diferença
entre dois horarios.
"""

class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo + segundos
        self.hora = total_segundos // 3600
        total_segundos %= 3600
        self.minuto = total_segundos // 60
        self.segundo = total_segundos % 60

    def diferenca_horaria(self, outro_horario):
        total_segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        diferenca_segundos = abs(total_segundos_atual - total_segundos_outro)
        hora_diff = diferenca_segundos // 3600
        diferenca_segundos %= 3600
        minuto_diff = diferenca_segundos // 60
        segundo_diff = diferenca_segundos % 60
        return hora_diff, minuto_diff, segundo_diff

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

# Exemplo de uso
horario1 = Horario(10, 30, 45)
horario2 = Horario(8, 45, 20)

print("Horário 1:", horario1)
print("Horário 2:", horario2)

# Incrementar segundos no Horário 1
horario1.incrementar_segundos(100)
print("Horário 1 após incrementar 100 segundos:", horario1)

# Diferença entre Horário 1 e Horário 2
diferenca = horario1.diferenca_horaria(horario2)
print("Diferença de Horário 1 para Horário 2:", f"{diferenca[0]} horas, {diferenca[1]} minutos, {diferenca[2]} segundos")
