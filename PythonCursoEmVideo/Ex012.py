preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 0.05)
print('O produto que custava R${}, na promoção com desconto de 5$ vai cutar R${}'.format(preço, novo))