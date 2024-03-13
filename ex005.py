n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print('\nA soma é: {};'.format(s), end='')
print('A subtração é: {};'.format(su))
print('A multiplicação é: {};'.format(m))
print('A divisão é: {:.3f};'.format(d))
print('O  produto é: {};'.format(p))
print('A divisãp inteira é: {};'.format(di))
print('O resto é: {}.'.format( r))