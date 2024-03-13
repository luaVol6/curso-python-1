from random import randint
from time import sleep
import colorsys
cmp = randint(0,5) #faz o sortei dos números, o computador pensa nisso
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = int(input('Em que número eu pensei? '))#jogador tenta adivinhar em que número o computador pensou
print('PROCESSANDO...')
sleep(3)
if num == cmp :
    print('Você acertou, o número que eu pensei foi o {}. PARABÉNS!!'.format(cmp))
else:
    print('Você errou!, o número que eu pensei foi o {} e não o {}. Mais sorte na próxima vez!'.format(cmp, num))
