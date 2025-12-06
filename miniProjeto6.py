#Mini-Projeto 6: A Calculadora de Frete Logístico

# Nossa regra de negócio será simples:
# Cada produto tem um valor base.
# O frete custa R$ 10,00 por quilo do produto.

# Precisamos criar uma função que receba o Valor do Produto e o Peso, e nos retorne o Total a Pagar (Produto + Frete).

# Definindo a ferramenta de cálculo
def calcular_total(valor_produto, peso_kg):
    valor_do_frete = peso_kg * 10
    total = valor_produto + valor_do_frete
    return total


# --- Interface do Sistema ---
print("--- Sistema de Logística ---")

# Pedindo dados ao usuário
v_prod = float(input("Qual o valor do produto? R$ "))
peso = float(input("Qual o peso (Kg)? "))

# Usando nossa ferramenta inteligente
valor_final = calcular_total(v_prod, peso)

print(f"O valor total com frete é: R$ {valor_final}")
