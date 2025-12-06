#Mini-Projeto 5: O “Cadastro” Centralizado

print("--- Bem-vindo ao Sistema de Cadastro (v2) ---")

# 1. Criamos um dicionário vazio para começar
cadastro = {}

# 2. Perguntamos ao usuário e salvamos direto nas chaves
# Observe: cadastro["nome da chave"] = valor digitado
cadastro["nome"] = input("Qual o seu nome? ")
cadastro["comida"] = input("Qual sua comida favorita? ")
cadastro["cidade"] = input("Onde você mora? ")

# 3. Gerar a Ficha
print("\n" + "=" * 30)
print("FICHA DE DADOS")
print("=" * 30)

# Usamos o loop para formatar bonito, sem precisar de vários prints manuais
for chave, valor in cadastro.items():
    # .capitalize() deixa a primeira letra da chave maiúscula (Nome, Comida...)
    print(f"{chave.capitalize()}: {valor}")
