import pygame
from redes import Red
import threading
red = Red()
updatedRed = True  # Va a comprobar si estamos actualizando la red
# actualizar interfaz
updateValue = False
pygame.init()
window_size = (600, 400)
window = pygame.display.set_mode(window_size)
# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Fuente
font = pygame.font.Font(None, 28)


def main():

    # Texto
    # Texto boton
    text = font.render("Iniciar Test Velocidad", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (300, 370)
    # Texto hosting
    txtHosting = font.render("Hosting", True, WHITE)
    txt_rectHosting = txtHosting.get_rect()
    txt_rectHosting.center = (300, 270)
    # Texto Subida
    txtSubida = font.render("Subida", True, WHITE)
    txt_rectSubida = txtSubida.get_rect()
    txt_rectSubida.center = (150, 220)
    # Texto Bajada
    txtBajada = font.render("Bajada", True, WHITE)
    txt_rectBajada = txtBajada.get_rect()
    txt_rectBajada.center = (450, 220)
    # Botón
    button_rect = pygame.Rect(250, 300, 100, 50)
    # gif
    imagePos = 0
    image = pygame.image.load("carga"+str(imagePos)+".jpg")
    cont = 0
    # pygame.display.set_caption("Animation")
    # Bucle principal
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:#pulsamos el boton
                mousePos = event.pos
                if button_rect.collidepoint(mousePos):
                    def update_speed():
                        global updatedRed, updateValue
                        updatedRed = False
                        red.update()
                        updatedRed = True
                        updateValue = True
                    thread = threading.Thread(target=update_speed)#cremos un hilo para consultar la velocidad
                    thread.start() #guardamos el hilo
            if (updateValue):
                #actualizamos los cuadros de texto
                txtHosting = font.render(red.host, True, WHITE)
                txt_rectHosting = txtHosting.get_rect()
                txt_rectHosting.center = (300, 270)
                txtSubida = font.render(red.upload, True, WHITE)
                txt_rectSubida = txtSubida.get_rect()
                txt_rectSubida.center = (140, 220)
                txtBajada = font.render(red.dowload, True, WHITE)
                txt_rectBajada = txtBajada.get_rect()
                txt_rectBajada.center = (450, 220)

        # Dibuja los elementos
        window.fill(BLACK)
        #Barra de carga
        if (not updatedRed):
            cont += 1
            if cont == 1400:
                cont = 0
                imagePos += 1
                image = pygame.image.load("carga"+str(imagePos)+".jpg")
                if imagePos == 4:
                    imagePos = -1
            window.blit(image, (190, 50))
        pygame.draw.rect(window, WHITE, button_rect)
        window.blit(text, text_rect)
        window.blit(txtHosting, txt_rectHosting)
        window.blit(txtBajada, txt_rectBajada)
        window.blit(txtSubida, txt_rectSubida)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
