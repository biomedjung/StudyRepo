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
