v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO, você excedeu o limite permitido que é 80km/h')
    m = (v-80)*7
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia, dirija com segurança"')