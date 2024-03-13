n = int(input('Digite um número qualquer: '))
res = n % 2
if res == 0:
    print('O número \033[0;33m{}\033[m é \033[0;35mPAR!\033[m'.format(n))
else:
    print('O número \033[0;35m{}\033[m é \033[0;33mIMPAR!\033[m'.format(n))