Sal = float(input('Qual é o Salário do funcionário? R$'))
novo = Sal + (Sal * 0.15)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(Sal, novo))