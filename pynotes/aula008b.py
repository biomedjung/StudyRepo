import random, emoji
num = random.random()  # float entre zero e um
numint = random.randint(1, 10)  # intervalo entre parenteses
print('random float (0 - 1): '.format(num), num)  # não entendi pq o format bugou......????
print('random integer (1 - 10): '.format(numint), numint)
print(num)
print(numint)
print(emoji.emojize('Olá mundo ! :bell:', use_aliases=True))
print(emoji.emojize(':biohazard:'))
