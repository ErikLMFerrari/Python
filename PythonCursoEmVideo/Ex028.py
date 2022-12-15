from random import randint
computador = randint(0, 5) #faz o computador "PENSAR"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
if jogador == computador:
     print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))