'''
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
print('Calculo do peso ideal')
altura1 = float(input('Digite a sua altura:'))
valor_se_homem = (altura1 * 72.7)
valor_1 = (valor_se_homem - 58)

valor_se_mulher = (altura1 * 62.1)
valor_2 = (valor_se_mulher - 44.7)
print('Peso ideal do homem:', valor_1)
print('Peso ideal da mulher:', valor_2)