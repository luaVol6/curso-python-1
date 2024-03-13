print('\033[0;35m-=\033[m'*12)
print('\033[0;33mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[0;35m-=\033[m'*12)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 +s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segentos acima \033[0;32mPODEM FORMAR UM TRIÂNGULO!\033[m')
else:
    print('Os segmentos acima \033[0;31mNÃO PODEM FORMAR UM TRIÂNGULO!\033[m')