from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano ==0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é BISSEXTO!'.format('\033[0;32;40m',ano,'\033[m'))
else:
    print('O ano {}{}{} NÃO É BISSEXTO!'.format('\033[0;31;40m',ano,'\033[m'))