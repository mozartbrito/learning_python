'''
2 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês.
'''
valorHora = float(input('Digite o valor que você ganha por hora: '))
horasTrabalhadas = float(input('Horas trabalhadas no mês:'))
salarioBruto = valorHora * horasTrabalhadas
ir = salarioBruto * 0.22
liquido = salarioBruto - ir
print('Salário brutol:     R$', salarioBruto)
print('Salário líquido:    R$', liquido)