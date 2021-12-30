# entra altura e largura da parede, devolve área em m^2 e quantidade de Litro de tinta (1L - 2m^2)
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('Para pintar uma parede com {} m de altura, e {} m de largura, com a área de {} m^2, utliza-se {} L de tinta.'
      .format(altura, largura, area, tinta))
