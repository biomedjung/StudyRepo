# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dist = float(input('Digite a distância percorrida: '))
dia = float(input('Digite a quantidade de dias alugados: '))
alug = dia * 60
fuel = dist * 0.15
pag = alug + fuel
print('O valor total a ser pago, BRL{} de aluguel + BRL{} de combustivel, somam BRL{}'.format(alug, fuel, pag))
