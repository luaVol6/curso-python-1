d = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
t = (d*60)+(km*0.15)
print('O total a pagar é de R${:.2f}!'.format(t))