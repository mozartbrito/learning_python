'''
3 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

(n1 * 2)  * (n2 / 2)
(3 * n1) + n3
n3 * n3 * n3 || n3 ** 3'''
num1 = int(input("Digite o 1º número, sendo ele inteiro: "))
num2 = int(input("Digite o 2º número, sendo ele inteiro:"))
num3 = float(input("Digite o 3º número, sendo ele real: "))

calculo_1 = ((num1 * 2) * (num2 / 2))
calculo_2 = num3 + (num1 * 3)
calculo_3 = num3 ** 3
print(f"O produto do dobro do primeiro com metade do segundo é igual a: {calculo_1}")
print(f"A soma do triplo do primerio com o terceiro é igual a: {calculo_2}")
print(f"O terceiro elevado ao cubo é igual a: {calculo_3}")