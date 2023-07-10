import time
import pygame
from unidecode import unidecode
from time import sleep
from unidecode import unidecode


print("=-" * 40)
print('\033[91m                 ======= Mercado Jcavi Delivery =========\033[0m'.center(50))
print("=-" * 40)


# Dicionário com os itens e seus respectivos preços
itens_mercado = {
    'Banana': 2.5,
    'Maçã': 3.0,
    'Laranja': 2.0,
    'Cenoura': 1.5,
    'Batata': 2.0
}

carrinho = []  # Lista para armazenar os itens escolhidos

print("Bem-vindo ao mercado!")
print("Aqui estão as opções de itens disponíveis:")

# Mostrar as opções de itens
for item, preco in itens_mercado.items():
    print(f"- {item} (R${preco:.2f})")


# Loop para escolher os itens
while True:

    escolha = input("Digite o nome do item que deseja adicionar (ou 'sair' para encerrar): ").lower()

    if escolha == 'sair':
        break

    # Remover acentos e caracteres especiais da escolha do usuário
    escolha_sem_acento = unidecode(escolha.lower())

    # Verificar se a escolha corresponde a um item do dicionário
    item_encontrado = False
    for item in itens_mercado.keys():
        item_sem_acento = unidecode(item.lower())
        if escolha_sem_acento == item_sem_acento:
            carrinho.append(item)
            item_encontrado = True
            print(f"Item '{item}' adicionado ao carrinho.")
            break

    if not item_encontrado:
        print("\033[91mItem não encontrado. Por favor, escolha outro.\033[0m")

print("Itens escolhidos:")
for item in carrinho:
    print(f"- {item.capitalize()}")

# Calcular o valor total
valor_total = sum(itens_mercado[item] for item in carrinho)

# Imprimir o valor total
print('\033[32mAguarde calculando...\033[0m')
time.sleep(3)
print(f"\033[34mValor total: R${valor_total:.2f}\033[0m")
time.sleep(1)

# Aqui a parte do pagamento - Menu de opções
print('-=-' * 10, 'PAGAMENTO', '-=-' * 10)
print('Como você deseja pagar por seus itens, escolha abaixo')
print('''[1] Dinheiro / Debito (5% Desconto)
[2] Cartão Credito (5% Acréscimo)
[3] Cartão Credito em mais de 2x (10% Acréscimo)''')
escolha_paga = int(input('Digite sua opção: '))

match escolha_paga:
    case 1:
        print(f'Você optou por \033[1m\033[4mAvista\033[0m e recebera 5% de desconto \033[91mR$ {valor_total - (valor_total * 5 / 100):.2f}\033[0m')
    case 2:
        print(f'Você optou por \033[1m\033[4mCredito a Vista\033[0m pagara com 5% de acréscimo \033[91mR$ {(valor_total * 5 / 100) + valor_total:.2f}\033[0m')
    case 3:
        print(f'Você optou por \033[1m\033[4mCredito em parcelas\033[0m e pagara com 10% de acréscimo \033[91mR$ {(valor_total * 10 / 100) + valor_total:.2f}\033[0m')

# Musica
while True:
    resposta = input("Deseja escutar uma musica em agradecimento [S]Sim/[N]Não): ").lower().split()[0]

    if resposta == 's':
        pygame.init()
        pygame.mixer.music.load('Super-Mario.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        input()
        pygame.event.wait()
    elif resposta == 'n':
        print("Volte sempre")
        break
    else:
        print("Resposta inválida. Por favor, digite [S]Sim - [N]Não.")




print("=-" * 40)
print('\033[91m                 ======= Agradecemos a Preferência =========\033[0m'.center(50))
print("=-" * 40)


