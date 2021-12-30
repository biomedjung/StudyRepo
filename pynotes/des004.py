# Faça um programa que leia algo que mostre na tela o seu tipo primitivo e todas as possiveis informações sobre
x = input('Digite algo: ')
print('O tipo primitivo de {} é: '.format(x), type(x))
print('O que foi digitado é alfabético? ', x.isalpha())
print('O que foi gigitado é numérico? ', x.isnumeric())
print('O que foi digitado é alfanumérico? ', x.isalnum())
print('O que foi digitado está tudo em maiúsculo? ', x.isupper())
print('O que foi digitado está tudo em minúsculo? ', x.islower())
print('O que foi digitado é somente espaço? ', x.isspace())
print('O que foi digitado está capitalizado? ', x.iscapitalize()) # primeira letra Maiúscula?

