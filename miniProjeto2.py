print("--- Bem-vindo ao Evento ---")
idade_texto = input("Qual é a sua idade? ")
idade = int(idade_texto)

if idade > 65:
    print("Você tem entrada grátis! Aproveite.")
elif idade >= 18:
    print("Sua entrada é R$ 20,00. Bem-vindo(a).")
else:
    print("Acesso permitido apenas para maiores de 18 anos.")

#Terminal: python miniProjeto2.py