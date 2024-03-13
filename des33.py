n1 =  int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('terceiro valor: '))
men = n1
if n2 < n1 and n2 < n3:
    men = n2
if n3 < n1 and n3 < n2:
    men = n3
print('O\033[0;40;35m menor \033[mvalor digitado foi: \033[0;30;45m {} \033[m'.format(men))

mai = n1
if n2>n1 and n2>n3:
    mai = n2
if n3 >n1 and n3>n2:
    mai = n3
print('O\033[0;30;45m maior \033[mvalor digitado foi: \033[0;40;35m {} \033[m'.format(mai))