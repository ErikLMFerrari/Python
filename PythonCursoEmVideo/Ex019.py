import random
N1 = str(input('Primeiro aluno: '))
N2 = str(input('Segundo aluno: '))
N3 = str(input('Terceiro aluno: '))
N4 = str(input('Quarto aluno: '))
lista = [N1, N2, N3, N4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')