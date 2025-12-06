# def mostra_nome(nome):
#     print(nome)

# mostra_nome('Rafael')

def converter_para_real(valor_em_dolar):
    cotacao = 5.50
    resultado = valor_em_dolar * cotacao
    return resultado

valor_convertido = converter_para_real(100)

print(f'O valor convertido é R$ {valor_convertido} ')