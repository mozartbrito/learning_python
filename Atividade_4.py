'''
4 - Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58'''

print('Calculo do peso ideal.')
altura1 = float(input('Digite a altura:'))
valor1 = (altura1 * 72.7)
valor2 = (valor1 - 58)
print('Peso ideal:', valor2)