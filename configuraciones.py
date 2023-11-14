import pygame
import sys,csv
#------------------------------------------------------------------------------------------------#
def reescalar_imagen(lista_imagenes,tamaño) -> None:
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],tamaño)

def girar_imagenes(lista_original:list,flip_x:int,flip_y:int) -> list:
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada

def obtener_rectangulos(principal:pygame.Rect) ->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -15, principal.width, 15)   
    diccionario["right"] = pygame.Rect(principal.right -15, principal.top, 15, principal.height)   
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 15, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 15)
    return diccionario
#------------------------------------------------------------------------------------------------#

#LISTA IMAGENES PERSONAJE
lista_img__quieto_derecha = [pygame.image.load("imagenes\personaje_principal\d1.png"),
                            pygame.image.load("imagenes\personaje_principal\d2.png")]
lista_img_quieto_izquierda = girar_imagenes(lista_img__quieto_derecha,True,False)
lista_img_saltando_derecha = [pygame.image.load("imagenes\personaje_principal\jump1.png"),
                              pygame.image.load("imagenes\personaje_principal\jump2.png")]
lista_img_saltando_izquierda = girar_imagenes(lista_img_saltando_derecha,True,False)
lista_img_derecha = [pygame.image.load("imagenes\personaje_principal\d1.png"),
                    pygame.image.load("imagenes\personaje_principal\d2.png"),
                    pygame.image.load("imagenes\personaje_principal\d3.png"),
                    pygame.image.load("imagenes\personaje_principal\d4.png"),
                    pygame.image.load("imagenes\personaje_principal\d5.png"),
                    pygame.image.load("imagenes\personaje_principal\d6.png"),
                    pygame.image.load("imagenes\personaje_principal\d7.png"),
                    pygame.image.load("imagenes\personaje_principal\d8.png")]
lista_img_izquierda = girar_imagenes(lista_img_derecha,True,False)
lista_img_recibir_daño = [pygame.image.load("imagenes/personaje_principal/recibir_daño_1.png")]
lista_img_muerte = [pygame.image.load("imagenes/personaje_principal/muerto_1.png")]
#------------------------------------------------------------------------------------------------#
#LISTA IMAGENES ENEMIGOS
lista_enemigo_izquierda = [pygame.image.load("imagenes/enemigo_nivel_1/enemigo_1.png"),
                           pygame.image.load("imagenes/enemigo_nivel_1/enemigo_2.png"),
                           pygame.image.load("imagenes/enemigo_nivel_1/enemigo_3.png"),
                           pygame.image.load("imagenes/enemigo_nivel_1/enemigo_4.png")]
lista_enemigo_derecha = girar_imagenes(lista_enemigo_izquierda,True,False)
lista_enemigo_recibir_daño = [pygame.image.load("imagenes/enemigo_nivel_1/enemigo_herido_1.png")]

lista_enemigo_izquierda_2 = [pygame.image.load("imagenes/enemigo_nivel_2/enemigo_izquierda_2 (1).png"),
                           pygame.image.load("imagenes/enemigo_nivel_2/enemigo_izquierda_2 (2).png"),
                           pygame.image.load("imagenes/enemigo_nivel_2/enemigo_izquierda_2 (3).png"),
                           pygame.image.load("imagenes/enemigo_nivel_2/enemigo_izquierda_2 (4).png")]
lista_enemigo_derecha_2 = girar_imagenes(lista_enemigo_izquierda_2,True,False)
lista_enemigo_recibir_daño_2 = [pygame.image.load("imagenes/enemigo_nivel_2/enemigo_herido_2 (1).png")]

lista_enemigo_izquierda_3 = [pygame.image.load("imagenes/enemigo_nivel_3/izquierda_enemigo_3 (1).png"),
                           pygame.image.load("imagenes/enemigo_nivel_3/izquierda_enemigo_3 (2).png"),
                           pygame.image.load("imagenes/enemigo_nivel_3/izquierda_enemigo_3 (3).png"),
                           pygame.image.load("imagenes/enemigo_nivel_3/izquierda_enemigo_3 (4).png")]
lista_enemigo_derecha_3 = girar_imagenes(lista_enemigo_izquierda_3,True,False)
lista_enemigo_recibir_daño_3 = [pygame.image.load("imagenes/enemigo_nivel_3/enemigo_herido_3 (1).png")]
#------------------------------------------------------------------------------------------------#