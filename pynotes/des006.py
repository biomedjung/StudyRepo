# código que pede um número, retorna o dobro, triblo, e raiz quadrada
n = int(input('Digite um valor inteiro:'))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('Sendo n = {} \n {} x 2 = {} \n {} x 3 = {} \n A raiz quadrada de {} vale {}'
      . format(n, n, dobro, n, triplo, n, raiz))
