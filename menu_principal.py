import pygame
from pygame.locals import *
from constantes import *
from configuraciones import *
from nivel_1 import Nivel_1
from nivel_2 import Nivel_2
from nivel_3 import Nivel_3
from puntaje import *
def menu():
    pygame.init()
    fuente = pygame.font.SysFont("Arial",20)
    texto_nivel_1 = fuente.render(str("Nivel 1"),True,NEGRO)
    texto_nivel_2 = fuente.render(str("Nivel 2"),True,NEGRO)
    texto_nivel_3 = fuente.render(str("Nivel 3"),True,NEGRO)
    texto_puntaje = fuente.render(str("Puntaje"),True,NEGRO)
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
    flag_ejecucion = True
    while flag_ejecucion:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_ejecucion = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                print(posicion_click)

                if (posicion_click[0] > 88 and posicion_click[0] < 238) and (posicion_click[1] > 265 and posicion_click[1] < 311): #nivel 1
                    Nivel_1()
                elif (posicion_click[0] > 327 and posicion_click[0] < 476) and (posicion_click[1] > 265 and posicion_click[1] < 311): #nivel 2
                    Nivel_2()
                elif (posicion_click[0] > 552 and posicion_click[0] < 698) and (posicion_click[1] > 265 and posicion_click[1] < 311): #nivel 3
                    Nivel_3()
                elif (posicion_click[0] > 328 and posicion_click[0] < 476) and (posicion_click[1] > 370 and posicion_click[1] < 421): #puntaje
                    lista_score = leer_csv("puntos.csv")
                    mostrar_puntajes(lista_score)
        pantalla.fill(VERDE)
        pygame.draw.rect(pantalla,BLANCO,(88,265,150,50)) #Rect nivel uno
        pygame.draw.rect(pantalla,BLANCO,(326,265,150,50)) #Rect nivel dos
        pygame.draw.rect(pantalla,BLANCO,(550,265,150,50)) #Rect nivel tres
        pygame.draw.rect(pantalla,ROJO,(328,370,150,50)) #Rect nivel tres
        
        pantalla.blit(texto_nivel_1,(135,281)) #texto nivel 1
        pantalla.blit(texto_nivel_2,(370,281)) #texto nivel 2
        pantalla.blit(texto_nivel_3,(600,281)) #texto nivel 3
        pantalla.blit(texto_puntaje,(368,380)) #texto nivel puntaje
        pygame.display.flip()
    pygame.quit
menu()
    