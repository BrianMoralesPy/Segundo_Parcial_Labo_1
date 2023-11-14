import pygame
import csv
import re
from constantes import *

def guardar_puntos_en_csv(nombre,puntos:int):
    with open('puntos.csv', 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([nombre,puntos])
def leer_csv(nombre_csv:str):
    '''
        esta funcion recibe el path del archivo csv para devolver una lista con los heroes 
        o devolver false si no encuentra nada
    '''
    valor_retorno = False
    try:
        lista_csv = []
        archivo = open(nombre_csv, 'r', encoding = "utf-8")
        for linea in archivo:
            lectura = re.split(",|\n",linea)
            dic_score = {}
            dic_score["nombre"] = lectura[0]
            dic_score["puntaje"] = int(lectura[1])
            lista_csv.append(dic_score)
        archivo.close()
        valor_retorno = lista_csv
    except FileNotFoundError:
        valor_retorno = False
    return valor_retorno

def mostrar_puntajes(lista_puntajes:list) -> None:

    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Puntajes")
    fuente = pygame.font.SysFont("Arial", 20)
    
    ejecutar = True
    while ejecutar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False

        pantalla.fill(VERDE)

        # Imprimir cada nombre y puntaje en una posición diferente
        y_pos = 35
        for diccionario in lista_puntajes:
            for clave, valor in diccionario.items():
                texto_puntaje = fuente.render(f"{str(clave)}: {str(valor)}", True, NEGRO)
                pantalla.blit(texto_puntaje, (77, y_pos))
                y_pos += 30  # Incrementar la posición vertical para el siguiente nombre y puntaje

        pygame.display.update()

