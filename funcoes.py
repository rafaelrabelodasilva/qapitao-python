# def mostra_nome(nome):
#     print(nome)

# mostra_nome('Rafael')

# def converter_para_real(valor_em_dolar):
#     cotacao = 5.50
#     resultado = valor_em_dolar * cotacao
#     return resultado

# valor_convertido = converter_para_real(100)

# print(f'O valor convertido é R$ {valor_convertido} ')

def criar_email_corporativo(nome, empresa):
    email = f'{nome}@{empresa}.com.br'
    return email.lower()


email_fernando = criar_email_corporativo('Fernando', 'Google')
email_papito = criar_email_corporativo('Papito', 'Tesla')
email_ana = criar_email_corporativo('Ana', 'Amazon')

print(email_fernando)
print(email_papito)
print(email_ana)
