* Exercício 1
* Exercício 2
* Exercício 3: crie um programa que leia dois números e mostre a soma entre eles

``` python
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {0} e {1} é igual a {2}'.format(n1, n2, s))

>>>Digite um número: 5
   Digite outro número: 6
   A soma entre 5.0 e 6.0 é igual a 11.0
```
* Exercício 4
* Exercício 5
* Exercício 6
* Exercício 7
* Exercício 8: lê um valor em metros, converte em cm e mm lê um valor em metros, converte em cm e mm

``` python
m = float(input('Digite a sua medida em metros: '))
cm = m * 100
mm = m * 1000
print('Sua medida de {} m equivale a {} cm e {} mm'.format(m, cm, mm))

>>>Digite a sua medida em metros: 150
   Sua medida de 150.0 m equivale a 15000.0 cm e 150000.0 mm
```
* Exercício 9:

``` python
# um programa que leia um número qualquer, e mostre sua tabuada
n = int(input('Digite um número para gerar a sua tabuada: '))
print('-'*10)
print('1 x {} = {}'.format(n, n * 1))
print('2 x {} = {}'.format(n, n * 2))
print('3 x {} = {}'.format(n, n * 3))
print('4 x {} = {}'.format(n, n * 4))
print('5 x {} = {}'.format(n, n * 5))
print('6 x {} = {}'.format(n, n * 6))
print('7 x {} = {}'.format(n, n * 7))
print('8 x {} = {}'.format(n, n * 8))
print('9 x {} = {}'.format(n, n * 9))
print('10 x {} = {}'.format(n, n * 10))
print('-'*10)

>>>Digite um número para gerar a sua tabuada: 7
   ----------
   1 x 7 = 7
   2 x 7 = 14
   3 x 7 = 21
   4 x 7 = 28
   5 x 7 = 35
   6 x 7 = 42
   7 x 7 = 49
   8 x 7 = 56
   9 x 7 = 63
   10 x 7 = 70
   ----------

```

* Exercício 10

``` python
# Converta um valor em Real para Dólar
real = float(input('Quantos reais você quer converter em dólar? '))
dolar = real * 0.178
print('BRL {:.2f} = USD {:.2f}'.format(real, dolar))

>>>Quantos reais você quer converter em dólar? 5
   BRL 5.00 = USD 0.89

```

* Exercício 11

``` pyhton
# entra altura e largura da parede, devolve área em m^2 e quantidade de Litro de tinta (1L - 2m^2)

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('Para pintar uma parede com {} m de altura, e {} m de largura, com a área de {} m^2, utliza-se {} L de tinta.'
      .format(altura, largura, area, tinta))

>>>Digite a altura da parede: 3
   Digite a largura da parede: 8
   Para pintar uma parede com 3.0 m de altura, e 8.0 m de largura, com a área de 24.0 m^2, utliza-se 12.0 L de tinta.

```
* Exercício 12
``` python
# preço, retora novo preço com 5% de desconto
p = float(input('Digite o valor do produto: '))
desc = p * 0.05
np = p - desc
print('O valor do produto com 5% de desconto é: {}'.format(np))

>>>Digite o valor do produto: 54
   O valor do produto com 5% de desconto é: 51.3

```
* Exercício 13
``` pyhton
# salario, novo salario com 15% de aumento
sal = float(input('Digite o salario: '))
aumento = sal * 0.15
novosal = sal + aumento
print('O novo salario vale: {}'.format(novosal))

>>>Digite o salario: 750
   O novo salario vale: 862.5

```
* Exercício 14
``` python

>>>

```
* Exercício 15
``` pyhton

>>>

```
* Exercício 16: input num Real -> output a parte inteira
``` python
from math import floor
n = float(input('Digite um numero Real: '))
z = math.trunc(n) # "trunca" o numero, cortanto a casa decimal, diferente de um floor, que arredonda para baixo
print('A porção inteira do numero Real {} é {}'.format(n, z))

>>>Digite um numero Real: 5.56
  A porção inteira do numero Real 5.56 é 5

```
* Exercício 17: inputa cateto oposto e adjacente, output hipotenusa

REFAZER UTILIZANDO MÓDULO ADEQUADAMENTE !!!!!!
``` python
import math
cata = float(input('Digite o valor do cateto adjacente: ')) # cateto adjacente
cato = float(input('Digite o valor do cateto oposto: ')) # cateto oposto
hipo = (cata ** 2) + (cato ** 2)  # hipotenusa^2 = cata^2 + cato^2
hipo = math.sqrt(hipo)
print('A hipotenusa vale: {}'.format(hipo))
>>>Digite o valor do cateto adjacente: 5
   Digite o valor do cateto oposto: 8
   A hipotenusa vale: 9.433981132056603

```
* Exercício 18: inputa ângulo qualquer, output valor do seno, cosseno e tangente
``` python
import math
ang = math.radians(float(input('Digite o valor do ângulo: ')))
print('O seno vale {}'.format(math.sin(ang)))
print('O cosseno vale {}'.format(math.cos(ang)))
print('A tangente vale {}'.format(math.tan(ang)))

>>>Digite o valor do ângulo: 58
   O seno vale 0.848048096156426
   O cosseno vale 0.5299192642332049
   A tangente vale 1.6003345290410507
   Digite o valor do ângulo: 58
   O seno vale 0.848048096156426
   O cosseno vale 0.5299192642332049
   A tangente vale 1.6003345290410507
```
* Exercício 19: Professor deseja sortear 1 aluno entre 4 para apagar o quadro. Input nome dos alunos, output 1 aluno aleatório
``` python
import random
aluno1 = input('Digite o nome de um aluno: ')
aluno2 = input('Digite o nome de mais um aluno: ')
aluno3 = input('Digite o nome de mais um aluno: ')
aluno4 = input('Digite o nome do último aluno: ')
turma = [aluno1, aluno2, aluno3, aluno4]
print(random.choice(turma))

>>>Digite o nome de um aluno: a
   Digite o nome de mais um aluno: b
   Digite o nome de mais um aluno: c
   Digite o nome do último aluno: d
   a

```
* Exercício 20: Mesmo professor quer definir a ordem de apresentação entre 4 alunos. Input 4 alunos, output uma ordem aleatória
``` python
import random
aluno1 = input('Digite o nome de um aluno: ')
aluno2 = input('Digite o nome de mais um aluno: ')
aluno3 = input('Digite o nome de mais um aluno: ')
aluno4 = input('Digite o nome do último aluno: ')
turma = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(turma)
print(turma)

>>>Digite o nome de um aluno: a
   Digite o nome de mais um aluno: b
   Digite o nome de mais um aluno: c
   Digite o nome do último aluno: d
   ['b', 'd', 'a', 'c']

```
* Exercício 21 Abre e reproduz um arquivo .mp3
``` python
import pygame
>>>

```
* Exercício 22: Ler nome e mostra com todas maiusc, todas minusc, quantas letras ao todo sem espaço, quantas letras no primeiro nome?
``` python

>>>

```
* Exercício 23: Ler entr 0 e 9999 e mostra cada um dos digitos separados, unidade, dezena, centena e milhar
``` python

>>>

```
* Exercício 24: Ler nome dee uma cidade e diz se começa ou não com o nome "SANTO"
``` python 

>>>

```
* Exercício 25: Ler nome e diz se tem "Silva"
``` python

>>>

```
* Exercício 26: Ler frase
Quantas vezes aparece letra "A"
Em que posição ela aparece a primeira vez?
Em que posição ela aparece a última vez?
``` python

>>>

```
* Exercício 27: Ler nome completo, mostrar primeiro nome e ultimo nome
``` python

>>>

```
* Exercício 28
``` python

>>>

```
* Exercício 29
``` python

>>>

```
* Exercício 30
``` python

>>>

```
* Exercício 31
``` python

>>>

```
* Exercício 32
``` python

>>>

```
* Exercício 33
``` python

>>>

```
* Exercício 34
``` python

>>>

```
* Exercício 35
``` python

>>>

```
* Exercício 36
``` python

>>>

```
* Exercício 37
``` python

>>>

```
* Exercício 38
``` python

>>>

```
* Exercício 39
``` python

>>>

```
* Exercício 40
``` python

>>>

```
* Exercício 41
``` python

>>>

```
* Exercício 42
``` python

>>>

```
* Exercício 43
``` python

>>>

```
* Exercício 44
``` python

>>>

```
* Exercício 45
``` python

>>>

```
* Exercício 46
``` python

>>>

```
* Exercício 47
``` python

>>>

```
* Exercício 48
``` python

>>>

```
* Exercício 49
``` python

>>>

```
* Exercício 50
``` python

>>>

```
* Exercício 51
``` python

>>>

```
* Exercício 52
``` python

>>>

```
* Exercício 53
``` python

>>>

```
* Exercício 54
``` python

>>>

```
* Exercício 55
``` python

>>>

```
* Exercício 56
``` python

>>>

```
* Exercício 57
``` python

>>>

```
* Exercício 58
``` python

>>>

```
* Exercício 59
``` python

>>>

```
* Exercício 60
``` python

>>>

```
* Exercício 61
``` python

>>>

```
* Exercício 62
``` python

>>>

```
* Exercício 63
``` python

>>>

```
* Exercício 64
``` python

>>>

```
* Exercício 65
``` python

>>>

```
* Exercício 66
``` python

>>>

```
* Exercício 67
``` python

>>>

```
* Exercício 68
``` python

>>>

```
* Exercício 69
``` python

>>>

```
* Exercício 70
``` python

>>>

```
* Exercício 71
``` python

>>>

```
* Exercício 72
``` python

>>>

```
* Exercício 73
``` python

>>>

```
* Exercício 74
``` python

>>>

```
* Exercício 75
``` python

>>>

```
* Exercício 76
``` python

>>>

```
* Exercício 77
``` python

>>>

```
* Exercício 78
``` python

>>>

```
* Exercício 79
``` python

>>>

```
* Exercício 80
``` python

>>>

```
* Exercício 81
``` python

>>>

```
* Exercício 82
``` python

>>>

```
* Exercício 83
``` python

>>>

```
* Exercício 84
``` python

>>>

```
* Exercício 85
``` python

>>>

```
* Exercício 86
``` python

>>>

```
* Exercício 87
``` python

>>>

```
* Exercício 88
``` python

>>>

```
* Exercício 89
``` python

>>>

```
* Exercício 90
``` python

>>>

```
* Exercício 91
``` python

>>>

```
* Exercício 92
``` python

>>>

```
* Exercício 93
``` python

>>>

```
* Exercício 94
``` python

>>>

```
* Exercício 95
``` python

>>>

```
* Exercício 96
``` python

>>>

```
* Exercício 97
``` python

>>>

```
* Exercício 98
``` python

>>>

```
* Exercício 99
``` python

>>>

```
* Exercício 100
``` python

>>>

```
* Exercício 101
``` python

>>>

```
* Exercício 102
``` python

>>>

```
* Exercício 103
``` python

>>>

```
* Exercício 104
``` python

>>>

```
* Exercício 105
``` python

>>>

```
* Exercício 106
``` python

>>>

```
* Exercício 107
``` python

>>>

```
* Exercício 108
``` python

>>>

```
* Exercício 109
``` python

>>>

```
* Exercício 110
``` python

>>>

```
* Exercício 111
``` python

>>>

```
* Exercício 112
``` python

>>>

```
* Exercício 113
``` python

>>>

```
* Exercício 114
``` python

>>>

```
* Exercício 115
``` python

>>>

```
* Exercício 116
``` python

>>>

```
* Exercício 117
``` python

>>>

```
* Exercício 118
``` python

>>>

```
* Exercício 119
``` python

>>>

```
* Exercício 120
``` python

>>>

```
* Exercício 121
``` python

>>>

```
* Exercício 122
``` python

>>>

```
* Exercício 123
``` python

>>>

```
* Exercício 124
``` python

>>>

```
* Exercício 125
``` python

>>>

```
