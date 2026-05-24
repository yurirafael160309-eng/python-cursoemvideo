dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos Km rodados?'))
cd = dias * 60
ckm = km * 0.15
total = cd + ckm
print('O total a pagar pelo carro é R${:.2f}'.format(total))