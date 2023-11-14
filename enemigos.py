import pygame
from configuraciones import *
from personaje import Personaje
class Enemigo:
    def __init__(self,tamaño_enemigo:tuple,posicion_inicial:tuple,animaciones:dict,trayectoria_final:int,velocidad:int,vida:int,vida_perdida:int):
        #enemigo
        self.ancho_enemigo = tamaño_enemigo[0]
        self.alto_enemigo = tamaño_enemigo[1]
        self.contador_frames = 0
        self.accion = None
        self.animaciones_enemigo = animaciones
        self.reescalar_animaciones_enemigo()
        self.velocidad_enemigo = velocidad
        self.desplazamiento_y = 0
        self.vida = vida
        self.vida_perdida = vida_perdida
        self.trayectoria = [posicion_inicial[0],trayectoria_final]
        self.animacion_derecha = animaciones["correr_derecha"]
        self.animacion_izquierda = animaciones["correr_izquierda"]
        #RECTANGULOS
        rectangulo_enemigo = self.animaciones_enemigo['correr_derecha'][0].get_rect()
        rectangulo_enemigo.x = posicion_inicial[0]
        rectangulo_enemigo.y = posicion_inicial[1]
        self.lados_enemigo = obtener_rectangulos(rectangulo_enemigo)
    
    def reescalar_animaciones_enemigo(self): # Reescalar diccionario de animaciones
        for animacion in self.animaciones_enemigo:
            reescalar_imagen(self.animaciones_enemigo[animacion],(self.ancho_enemigo, self.alto_enemigo))
    
    def animar_enemigo(self,pantalla): # Animar al enemigo
        if self.contador_frames + 1 >= 3:
            self.contador_frames = 0
            
        if self.velocidad_enemigo > 0:
            pantalla.blit(self.animacion_derecha[self.contador_frames // 1],self.lados_enemigo["main"])
            self.contador_frames += 1
        else:
            pantalla.blit(self.animacion_izquierda[self.contador_frames // 1],self.lados_enemigo["main"])
            self.contador_frames += 1
    
    def animar_enemigo_2(self,pantalla,que_animacion:str): # Animar al enemigo
        animacion = self.animaciones_enemigo[que_animacion]
        longitud_animacion = len(animacion)
        if self.contador_frames >= longitud_animacion:
            self.contador_frames = 0
        pantalla.blit(animacion[self.contador_frames],self.lados_enemigo["main"])
        self.contador_frames += 1

    def mover_enemigo(self, velocidad:int): # Mover al enemigo
        if self.velocidad_enemigo > 0:
            for lados in self.lados_enemigo:
                if self.lados_enemigo[lados].x < self.trayectoria[1] + self.velocidad_enemigo:
                    self.lados_enemigo[lados].x += velocidad
                else:
                    self.velocidad_enemigo = self.velocidad_enemigo * -1
                    self.lados_enemigo[lados].x += velocidad
        else:
            for lados in self.lados_enemigo:
                if self.lados_enemigo[lados].x > self.trayectoria[0] - self.velocidad_enemigo:
                    self.lados_enemigo[lados].x += velocidad
                else:
                    self.velocidad_enemigo = self.velocidad_enemigo * -1
                    self.lados_enemigo[lados].x += self.velocidad_enemigo

    def colision_con_personaje(self,pantalla,personaje): #colision de enemigos con el personaje
        if self.lados_enemigo["top"].colliderect(personaje.lados_personaje["bottom"]):
            self.animar_enemigo_2(pantalla,"recibir_daño")
            self.vida -= self.vida_perdida
            print(f"vida enemigo ={self.vida}")
    def esta_muerto(self):
        return self.vida <= 0

    def update(self,pantalla,personaje): #Actualiza la pantalla con el movimiento y la animacion del enemigo
        self.animar_enemigo(pantalla)
        self.mover_enemigo(self.velocidad_enemigo)
        self.colision_con_personaje(pantalla,personaje)
