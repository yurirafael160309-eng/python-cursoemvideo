produto = float(input('Digite o preço do produto: R$'))
desconto = int(input('Agora, digite a promoção. %'))
novo = produto - (produto * desconto/100)
print('O produto que custava R${:.2f}, com o desconto de %{} custará {:.2f}!!!'.format(produto,desconto,novo))