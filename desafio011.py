largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
soma = largura * altura
divisao = soma / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m². Para pintar essa parede você irá precisa de {:.2f}L de tinta'.format(largura,altura,soma,divisao))