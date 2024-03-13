# MANIPULANDO TEXTO

frase = 'curso em video'
print(frase[9:14:1]) #Fatia a frase, o ':' serve como delimitador até.
# [9]  -  escolhe apenas a letra que está na posição 9
# [:5]  - a primeira letra está na posição 0 e vai até o 4
# [15;]  - começa no 15 e acaba na ultima letra
# [9:12:2]  - o número que vem depois dos segundo : é a quantidade de casas que vai pulando entre os números dados, 9, 11.
# [9::3]  - o do meio vazio significa que vai até o final

# len(frase)  -  mostra o comprimento da frase
# frase.count('o')  -  conta quantas vezes a letra aparece, nesse caso o 'o'
# frase.count('o',0,13)  - conta as letras do 0 até o 12, o python ignora o ultimo número
#frase.find('deo')  -  indica em que posição a primeira letra da frase aparece, e se você receber o valor -1 significa que a palavra não foi encontrada
# 'curso' in frase  -  mostra se a palavra existe na frase ou não, com true ou false
#frase.replace('python', 'android')  - troca as palvras, substituindo uma pela outra
#frase.upper()  - transforma a frase em maiuscula
#frase.lower()  - transforma a frase em minuscula
#frase.capitalize()  - transforma a frase em minuscula, só não a primeira letra
#frase.title()  - transforma a primeira letra de todas as palavras em maiusculas

#frase.strip()  - remove os espaços do começo e do fim da frase, por eles não serem necessarios
#frase.rstrip()  - remove apenas os espaços da direita -rigth
#frase.lstrip()  - remove apenas os espaços da esquerda - left

#frase.split() - divide as palavras, assim cada palavra vai ser uma lista
#'-'.jois(frase) - junta as palavras separando elas com '-'  ex: problema-resolvido