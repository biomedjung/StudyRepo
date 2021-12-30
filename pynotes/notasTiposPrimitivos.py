 int = (7 , -4 , 0 , 9878)
 float = (4.5, 0,78, -15.28, 7.0)
 bool = True or False
 str = 'Olá mundo', '7.5', '' #string vazia

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print('a soma entre: ', n1, 'e', n2, ' é igual a: ', s) ----- formato antigo
print('A soma entre {0} e {1} vale {2}'. format(n1, n2, s)) # formato mais recente

n = float(input('Digite um valor: ')) # bool True se tem valor,
print(type(n))
print(n.isalpha()) # varios is
