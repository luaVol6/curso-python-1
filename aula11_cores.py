#\033[0style;text;backgroundm]

# style = 0 -> nada, 1 -> bold, 4 -> underline (sublinha), 7 -> negative (inverte o fundo com o texto)

# text = 30 - black, 31 - red, 32 - green, 33 - yellow, 34 - blue, 35 - magenta, 36 - cyan, 37 - grey, 97 - white

# back = 40 - black, 41 - red, 42 - green, 43 - yellow, 44 - blue, 45 - magenta, 46 - cyan, 47 - grey, 107 - white

print('\033[7;36;40mOlá, mundo!\033[m')
print('\033[1;107;42mLarry is real!\033[m')

a = 28
b = 1994
print('Os valores são \033[33m{}\033[m e \033[35m{}\033[m!!'.format(a, b))

nome = 'Lua'
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco': '\033[0;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome,cores['limpa']))

#print('Olá, muito prazer em te conhecer, {}{}{}!'.format('\033[7;97;40m', nome, '\033[m)'))