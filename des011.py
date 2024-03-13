l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l*h
p = a/2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m². \nPara pintar essa parede você precisará de {}l de tinta.' .format(l, h, a, p))