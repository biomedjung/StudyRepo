# Montar um programa que pede um número, mostra seu antecessor e seu sucessor
n = int(input('Digite um valor inteiro: '))
ant = n - 1
suc = n + 1
print('O antecessor de {} vale {}, e o sucessor vale {}'.format(n, ant, suc))
