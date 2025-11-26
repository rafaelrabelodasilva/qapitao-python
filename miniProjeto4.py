# Mini-Projeto 4: O Validador de Senha
# Programa que só continua quando o usuário digitar a senha correta

senha_secreta = "python123"
senha_digitada = "" # Só para inicializar a variável

while senha_digitada != senha_secreta:
    print("--- Sistema de Segurança ---")
    senha_digitada = input("Por favor, digite a senha: ")

    if senha_digitada == senha_secreta:
        print("Acesso Concedido!")
    else:
        print("Senha incorreta. Tente novamente.")

print("Programa finalizado.")

#Terminal: python miniProjeto4.py