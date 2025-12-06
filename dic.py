pessoa = {
  'nome': 'Rafael Rabelo da Silva',
  'idade': 29,
  'cidade': 'Criciúma',
  'ativo': True
}

# print(pessoa['cidade'])

pessoa['idade'] = 30
pessoa['profissão'] = 'QA'
# print(pessoa)

for chave in pessoa:
  print(chave)

for chave, valor in pessoa.items():
  print(f'A chave {chave} guarda o valor {valor}')