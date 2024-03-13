frs = str(input('Digite uma frase: ')).lower().strip()
print('A letra A apareceu {} vezes na frase.'.format(frs.count('a')))
print('A primeira letra A apareceu na posição {}.'.format(frs.find('a')+1))
print('A ultima letra A apareceu na posição {}.'.format(frs.rfind('a')-1))

#Amanda ama pedro