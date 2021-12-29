## Python
# Variables
  Assingment
# Data Types
# Operations
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
