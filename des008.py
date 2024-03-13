n = float(input('Digite uma distância em metros: '))
#km = n/1000
#hm = n/100
#dam = n/10
#dm = n*10
#cm = n*100
#mm = n*1000
print('A medida de {}m corresponde a: \nQuilômetros: {}km; \nHectômetros: {}hm; \nDecâmetros: {}dam; \nDecímetros: {:.0f}dm; \nCentímetros: {:.0f}cm; \nMilímetros: {:.0f}mm.'.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))