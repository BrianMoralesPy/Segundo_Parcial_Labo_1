import pygame
from configuraciones import *
class Item:
    def __init__(self,tamaño:tuple,coordenadas:tuple,imagen_item:str):
        self.ancho_item = tamaño[0]
        self.alto_item = tamaño[1]
        self.imagen = pygame.image.load(imagen_item)
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho_item,self.alto_item))
        rectangulo_item = self.imagen.get_rect()
        rectangulo_item.x = coordenadas[0]
        rectangulo_item.y = coordenadas[1]
        self.lados_item = obtener_rectangulos(rectangulo_item)
    def update(self,pantalla:pygame.display.set_mode):
        pantalla.blit(self.imagen,self.lados_item["main"])