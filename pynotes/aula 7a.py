nome = str(input('Qual seu nome?'))
print('Olá {}, vou te pedir alguns números!'.format(nome))

# {:X} o numero dentro da mascara de substituição {:>20} alinha a direita em vinte espaços
# < esquerda ^centraliza
# :=^ centralizado, com iguais nos espaços

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))

soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
modulo = n1 % n2
exp = n1 ** n2
raiz = n1 ** (1/n2)

print('Se n1 = {} e n2 = {}'.format(n1, n2))
print('A soma vale {}, o resto da subtração vale {}'.format(soma, subt))
print('O produto da multiplicação vale {}, \n o quociente da divisão vale {:.3f}'.format(mult, div), end=' ')
print('O quociente da divisão inteira vale {}, e o resto vale {}'.format(divint, modulo))
print('A potência de {} elevado a {} vale {}, e a raiz de índice {} de {} vale {:.3f}'.format(n1, n2, exp, n2, n1, raiz))

# \n = nova linha
# end='' significa que a linha vai terminar em NADA, ou seja, não vai quebrar a linha
# .3f = até 3 casas decimais float
