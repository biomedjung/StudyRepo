## Python
identation - tab = 4 spaces

## Reserved Words
and
except
lambda
with
as
finally
nonlocal
while
assert
false
None
yield
break
for
not
class
from
or
continue
global
pass
def
if
raise
del
import
return
elif
in
True
else
is
try

# Variables
Um lugar nomeado, na memória, onde podemos armazenar dados
  Assingment
  '=' assingment statemante
``` python
>>> x = 1.2
``` 
# Constants
 Valores fixos
 ``` python
>>> print('hello world')
 ```
 
# Data Types Tipos Primitivos
Half Types: Literals, Variables, Constants
``` python
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
```
``` python
# Aula 06 Curso em vídeo py01
n1 = int(input('Digite um número: ')) #= se le como "recebe"
n2 = int(input('Digite un múmero: '))
print(type(n2))
s = int(n1) + int(n2)
print('A soma vale {}'.format(s))
```

## Strings

``` python
nome = "Palosity Academy"

print(nome)
print("onde \"exercitamos\" \n a palosidade\n" )     #:  \ serve para interpretar literalmente o simbolo que vier a seguir

print(nome + " é daora") # colocar mais coisa na string = CONCATENATION

#funcions para moidificar ou ter informações sobre STRING

print(nome.lower())
print(nome.isupper()) #verifica se é tudo maiúscula
print(nome.upper().isupper()) #mudamos para maiúscula

print(len(nome)) #quantos caracteres
print(nome[0]) #:  0 é o primeiro número indexado  P = 0 a = 1 l = 2 etc.
print(nome[3])

print(nome.index("P")) #dá a posição #PARAMETRO = valor que se dá a uma função
print(nome.index("Aca"))

print(nome.replace("Palosity", "Bananas"))
```
# Operations
``` python
# Aula 07 Curso em vídeo py01
5 + 2 == 7 # + adição   | Também concatena String
5 - 2 == 3 # - subtração
5 * 2 == 10 # * multiplicação  | Funciona em string
5 / 2 == 2.5 # / divisão
5 ** 2 == 25 # ** potência
5 // 2 == 2  # // divisão inteira, sobra 1
5 % 2 == 1 # % remainder, resto da divisão OU módulo,  o mesmo 1 que sobrou
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
# - 5 Esquerda p di

n1 = int(input('Digite um número: ')) #= se le como "recebe"
n2 = int(input('Digite un múmero: '))
s = n1 + n2
print('A soma vale {}'.format(s)) # {} mascara de substuição

 # o limite do python é a própria memória, isso permite grandes cálculos
```

``` python
from math import *   # Dá acesso a várias funções matemáticas

print(-7.0987)
print((3 + 4.7) * 8)   # + - / *
print(10 % 3)   # "ten mod three" - vai pegar o primeiro número, dividir pelo segundo, e dar o RESTO

my_num = 7
print(str(my_num) + " is my favorite number")  # transforma o número em uma string
# print(my_num + "is my favorite number") DARIA ERRO, precisa transformar em string para imprimir do lado de uma string

# FUNCIONS

print(abs(my_num))  # R: 7  dá o valor absoluto
print(pow(3, 2))    # R: 9  3^2
print(max(10, 2))   # R: 10 maior valor
print(min(10, 2))   # R: 2  menor valor
print(round(3.2))   # R: 3
print(round(3.7))   # R: 4

print(floor(3.7))   # R: 3  arredonda para baixo
print(ceil(3.2))    # R: 4  arredonda para cima
print(sqrt(36))     # R: 6  raiz quadrada
```
# Lists

# Functions

``` python
def nomeDaFunccao()
    print('Voce invocou a função chamada nomeDaFunção, Parabéns!')
    x = input('Qual o seu nome?')
    print('então,' + x + ', vá se foder e não me invoque novamente!')
print('Olá, eu sou um bom software, tenho uma função chamada nomeDaFunccao(), tente usar!')

### def define a função, a parte identada define a função, só grava na memoria
### posteriormente invocar//call
assignment = funciont('Argument')  ###passa a função no argumento
type()
float()
input() ### returns string
int()  ### turns into int

### podemos criar novas palavras reservadas

print() ###is a buit in funciont
```
---
``` python
>>> 5 == 5
True
>>> 5 == 6
False
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
x is y               # x is the same as y
x is not y           # x is not the same as y
```
Conditional Execution Identação Python é sensível à identação, continuar até o fim do bloco. Identar depois do if 4 spaces para cada identação, pyhton pode se confundir com Tab (atom faz automatico). Podemos fazr quantos nested blocks quisermos
``` python
x = 5
if x > 2 : # if block starts with a statement
    print('Bigger than 2') # bloco interno
    print('Still bigger') # bloco interno
print('Done with 2') # print não conta

for i in range(5) : # first statement
    print(i)
    if i > 2 :   # second statement
        print('Bigger than 2') # end of second block
    print('Done with i', i) # end of the first
print('All')
```
``` python
x = 5
if x < 10:
	print('smaller')
if x > 20:
	peint('bigger')
print('finis')
```
## Repeated steps
``` python
# repetir bloco identado enquanto for verdadeiro
n = 5
while n > 0:
	print(n):
	n = n-1
print('blastoff!')
````
	
## Nested Decisions
``` python
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')
```
## 2 Branch if, fork
```
x = 4
if x > 2 :
    print('Bigger')
else
    print('Smaller')
print('All done')
```
## Multi-Way
Elif: se a primeira positiva, vai pro final do bloco, só uma executa o bloco
```` python
x = 0
if x < 2 :
    print("Small")
elif x < 10 :
    print('Medium')
else :
    print('Large')
print ('All Done!')
````
 try/except
 proteção contra erros causados imputs ou algum outro erro, evita traceback error

antecipar um erro

``` python
# Aula 07 py01 curso em video
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
```

## IF ELSE
``` python
x = 4
if x > 2 :
    print('Bigger')
else : #Alternative if yes, if not (else)
    print('Smaller')

print 'All done'

print('Agent, looks like we identified some weird alien CODE')
print('It says:')
print('blip()'+"'bla'" +"'ble'"+"....................." )
print('YOUR JOB TODAY IS TO UNDERSTAND IT, CUZ IF THIS SHIT IS REAL WE HAVE TO KIDNAP ELON MUSK RIGHT NOW')

def blip(blorg):
	if blorg == 'bla':
		print('BLirg Blu litri blurgo blin bra zzzzzzzzzzzz tt')
	elif blorg == 'ble':
		print('RaZNuuuuuçpa tata blurgo blw 3214')
	elif blorg == 'bli':
        print('Ztrata tu temp 2...345..12,33333 aaaaaaaaa bli xsk')
        print('...')

    else print('Dumb american, its only bla, ble and bli. Retarded')

x = blip()
```
## LOOP While
```` python
n = 5
while n > 0:
    print(n)
    n = n-1

print('Blastoff!')
print(n)
````

 Aula O8
```` python
from math import sqrt
num = int(input('Digite um número: '))
raiz = math.sqrt(num) # sqrt(num)
print('Raiz de {} = {:.2f}'.format(num, raiz))
````
```` python
import random, emoji
num = random.random()  # float entre zero e um
numint = random.randint(1, 10)  # intervalo entre parenteses
print('random float (0 - 1): '.format(num), num)  # não entendi pq o format bugou......????
print('random integer (1 - 10): '.format(numint), numint)
print(num)
print(numint)
print(emoji.emojize('Olá mundo ! :bell:', use_aliases=True))
print(emoji.emojize(':biohazard:'))
````

```` python
# Bibliotecas, importações
import bibliotecas # mais generalista
from bibliotecas import coisaEspecifica # importa coisa especifica
import math
ceil # arredonda pra cima
floor # arredonda pra baixo
trunc # corta a parte decimal
pow() # expo
sqrt # raiz quadrada
factorial

from math import sqrt
````
