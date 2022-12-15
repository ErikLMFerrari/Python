salário = float(input('Qual é o salário do funcionário?'))
if salário <= 1250:
    novosalário = salário + (salário * 0.15)
else:
    novosalário = salário + (salário * 0.10)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. '.format(salário, novosalário))