d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km!'.format(d))
if d <200:
    print('E o preço da sua passagem será de R${}{:.2f}{}'.format('\033[1;97;40m',d*0.50,'\033[m'))
else:
    print('E o preço da sua passagem será de R${}{:.2f}{}'.format('\033[1;30;107m',d*0.45,'\033[m'))