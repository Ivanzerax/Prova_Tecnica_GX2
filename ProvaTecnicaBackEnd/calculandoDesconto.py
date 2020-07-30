valor = float(input('Digite um valor em reais: R$ '))
desconto = float(input('Digite a porcentagem de desconto a ser aplicada: '))
valorDesconto = valor * desconto / 100
valorFinal = valor - valorDesconto
print('O valor do desconto será de R${:.2f}'.format(valorDesconto))
print('O valor com o desconto aplicado será de R${:.2f}'.format(valorFinal))
