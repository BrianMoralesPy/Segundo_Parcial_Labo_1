import pygame
from configuraciones import *
class Plataforma:
    def __init__(self,tamaño:tuple,coordenadas:tuple,imagen_plataforma:str):
        self.ancho_plataforma = tamaño[0]
        self.alto_plataforma = tamaño[1]
        self.imagen = pygame.image.load(imagen_plataforma)
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho_plataforma,self.alto_plataforma))
        rectangulo_plataforma = self.imagen.get_rect()
        rectangulo_plataforma.x = coordenadas[0]
        rectangulo_plataforma.y = coordenadas[1]
        self.lados_plataforma = obtener_rectangulos(rectangulo_plataforma)
    def update(self,pantalla:pygame.display.set_mode):
        pantalla.blit(self.imagen,self.lados_plataforma["main"])