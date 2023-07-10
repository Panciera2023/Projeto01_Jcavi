import pygame

# pygame.init()
# pygame.mixer.music.load('Super-Mario.mp3')
# pygame.mixer.music.play(loops=0, start=0.0)
# input()
# pygame.event.wait()


resposta = input("Deseja executar o código? (sim/não): ")

if resposta.lower() == "sim":
    pygame.init()
    pygame.mixer.music.load('Super-Mario.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    input()
    pygame.event.wait()
elif resposta.lower() == "não":
    print("Código não será executado.")
else:
    print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
