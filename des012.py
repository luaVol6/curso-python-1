v = float(input('Qual o preço do produto: R$'))
r = v-(v*5/100)
print('o produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.' .format(v, r))