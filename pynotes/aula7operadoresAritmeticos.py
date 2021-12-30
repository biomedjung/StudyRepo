5 + 2 == 7 # + adição   | Também concatena String
5 - 2 == 3 # - subtração
5 * 2 == 10 # * multiplicação  | Funciona em string
5 / 2 == 2.5 # / divisão
5 ** 2 == 25 # ** potência
5 // 2 == 2  # // divisão inteira, sobra 1
5 % 2 == 1 # % resto da divisão OU módulo,  o mesmo 1 que sobrou
# == é igual?
# = recebe
pow (4,2) #  == 4 ** 2
81**(1/2) # == raiz quadrada
127**(1/3) # == raiz cubica

# Ordem de precedência
# - 1 ( )
# - 2 **
# - 3 *  /  //  % (quem aparece primeiro, se juntos)
# - 4 + -

n1 = int(input('Digite um número: ')) #= se le como "recebe"
n2 = int(input('Digite un múmero: '))
s = n1 + n2
print('A soma vale {}'.format(s)) # {} mascara de substuição

 # o limite do python é a própria memória, isso permite grandes cálculos