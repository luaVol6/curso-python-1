n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média final é {:.1f}!'.format(m))
if m <= 5.0:
    print('Você não passou de ano, sinto muito :(')
else:
    print('Você passou de ano, parabéns :)')