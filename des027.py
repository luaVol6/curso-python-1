nome = str(input('Digite seu nome completo: ')).strip()
nm = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}.'.format(nm[0]))
print('Seu último nome é: {}.'.format(nm[len(nm)-1]))