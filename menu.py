#Comando break para sair do loop

while True:
    comando = input('Digite sair para fechar o programa: ')

    if comando == 'sair':
        print('Até logo!')
        break
    else:
        print(f'Você digitou: {comando}')

#Terminal: python menu.py