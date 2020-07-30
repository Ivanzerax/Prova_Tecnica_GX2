def leiaInt(msg):
    validado = False
    valor = 0
    while True:
        cpf = str(input(msg))
        if cpf.isnumeric() and len(cpf) == 11:
            valor = int(cpf)
            validado = True
        else:
            print('Erro, campos inválidos!')
        if validado:
            break
    return valor

cpf = leiaInt('Digite um CPF para saber se ele é válido: \n')
print('Este CPF é válido!')
