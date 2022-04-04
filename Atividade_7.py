'''
7 - Faça um Programa que peça dois números e imprima o maior deles.
'''
diferente = True
n1 = float(input("Digite um numero:"))
n2 = float(input("Digite um numero:"))

while(n1 == n2):
    n2 = float(input("Digite o numero 2 outra vez, não podem ser iguais:"))

if n1 > n2:
    maior = n1
if n2 > n1:
    maior = n2
    print('O numero', maior, 'é o maior')
