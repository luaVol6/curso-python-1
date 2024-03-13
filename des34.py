s = float(input('\033[0;30;107mQual é o salário do funcionário?\033[m R$'))
if s <= 2000:
    print('Quem ganhava \033[0;31mRS{:.2f}\033[m passa a ganhar \033[0;32mR${:.2f}\033[m agora.'.format(s, s + s * 15/100))
else:
    print('Quem ganhava \033[0;31mRS{:.2f}\033[m passa a ganhar \033[0;32mR${:.2f}\033[m agora.'.format(s, s + s * 10/100))