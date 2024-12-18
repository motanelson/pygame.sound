import pygame
import sys

def main():
    # Inicializar o Pygame
    pygame.init()

    # Perguntar o nome do ficheiro de som
    sound_file = input("Digite o nome do ficheiro de som (com extensão .wav, .mp3, etc.): ").strip()

    try:
        # Carregar o som
        sound = pygame.mixer.Sound(sound_file)
        print(f"Som carregado: {sound_file}")
    except FileNotFoundError:
        print("Ficheiro de som não encontrado. Verifique o nome e tente novamente.")
        return
    except pygame.error as e:
        print(f"Erro ao carregar o som: {e}")
        return

    # Reproduzir o som
    sound.play()
    print("Reproduzindo som...")

    # Aguardar o fim da reprodução
    while pygame.mixer.get_busy():
        pygame.time.wait(100)  # Esperar por 100 ms para evitar uso excessivo da CPU

    print("Reprodução concluída. Saindo...")

    # Encerrar o Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
