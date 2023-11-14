import pygame
from configuraciones import *
class Personaje:
    def __init__(self,tamaño_personaje:tuple,posicion_inicial:tuple,animaciones:dict,velocidad:int,vidas:int,vidas_a_sumar:int,puntos_a_sumar:int):
        #PERSONAJE
        self.ancho_personaje = tamaño_personaje[0]
        self.alto_personaje = tamaño_personaje[1]
        self.contador_frames = 0
        self.accion = None
        self.animaciones_personaje = animaciones
        self.reescalar_animaciones_personaje()
        self.velocidad_personaje = velocidad
        self.desplazamiento_y = 0
        self.vidas = vidas
        self.puntos = 0
        self.puntos_a_sumar = puntos_a_sumar
        self.muerto = False
        self.win = False
        self.vidas_aumento = vidas_a_sumar
        
        #RECTANGULOS
        rectangulo_personaje = self.animaciones_personaje['quieto_derecha'][0].get_rect()
        rectangulo_personaje.x = posicion_inicial[0]
        rectangulo_personaje.y = posicion_inicial[1]
        self.lados_personaje = obtener_rectangulos(rectangulo_personaje)
        
        #GRAVEDAD
        self.gravedad_personaje = 1
        self.potencia_salto_personaje = -18
        self.limite_vel_caida_personaje = 18
        self.esta_saltando = False
    
    def reescalar_animaciones_personaje(self): # Reescalar diccionario de animaciones
        for animacion in self.animaciones_personaje:
            reescalar_imagen(self.animaciones_personaje[animacion],(self.ancho_personaje, self.alto_personaje))
    
    def animar_personaje(self,pantalla,que_animacion:str): # Animar al personaje
        animacion = self.animaciones_personaje[que_animacion]
        longitud_animacion = len(animacion)
        if self.contador_frames >= longitud_animacion:
            self.contador_frames = 0
        pantalla.blit(animacion[self.contador_frames],self.lados_personaje["main"])
        self.contador_frames += 1
    
    def mover_personaje(self, velocidad): # Mover al personaje
        for lado_personaje in self.lados_personaje:
            self.lados_personaje[lado_personaje].x += velocidad
    
    def aplicar_gravedad_personaje(self, pantalla,lista_plataformas:list): #Aplicar gravedad y detectar
        if self.esta_saltando:
            self.animar_personaje(pantalla, "saltar_derecha")
            for lado_personaje in self.lados_personaje:
                self.lados_personaje[lado_personaje].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad_personaje < self.limite_vel_caida_personaje:
                self.desplazamiento_y += self.gravedad_personaje
        
        for plataforma in lista_plataformas:
            if self.lados_personaje["bottom"].colliderect(plataforma.lados_plataforma["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados_personaje["main"].bottom = plataforma.lados_plataforma["main"].top + 1
                break
            else:
                self.esta_saltando = True
    
    def aplicar_colision_enemigo(self, pantalla, lista_enemigos):
        if not self.muerto:  # Verifica si el personaje no ha muerto
            if not self.win:
                for enemigo in lista_enemigos:
                    if self.lados_personaje["bottom"].colliderect(enemigo.lados_enemigo["top"]):
                        self.puntos += self.puntos_a_sumar
                        print(f"puntos {self.puntos}")
                        if self.puntos >= 120:
                            print("ganaste")
                            self.win = True
                            break
                    elif self.lados_personaje["right"].colliderect(enemigo.lados_enemigo["left"]):
                        self.animar_personaje(pantalla, "recibir_daño")
                        self.vidas -= 1
                        print(f"vidas {self.vidas}")
                        if self.vidas == 0:
                            self.muerto = True  # Marcar al personaje como muerto
                            self.accion = "muerte"  # Cambiar la acción a "muerte"
                        break
                    elif self.lados_personaje["left"].colliderect(enemigo.lados_enemigo["right"]):
                        self.animar_personaje(pantalla, "recibir_daño")
                        self.vidas -= 1
                        print(self.vidas)
                        if self.vidas == 0:
                            self.muerto = True
                            self.accion = "muerte"
                        break
    def aplicar_colision_items(self, pantalla, lista_items): #Aplico colision con los items
        items_a_eliminar = []
        for item in lista_items:
            if self.lados_personaje["main"].colliderect(item.lados_item["main"]):
                self.vidas += self.vidas_aumento
                items_a_eliminar.append(item)
                print(f"+{self.vidas} de vida")
        for item in items_a_eliminar:
            lista_items.remove(item)
    
    def update(self,pantalla,lista_plataformas:list,lista_enemigos:list,lista_items:list):
        if not self.muerto:
            if not self.win:
                match self.accion:
                    case "correr_derecha":
                        if not self.esta_saltando:
                            self.animar_personaje(pantalla,"correr_derecha")
                        self.mover_personaje(self.velocidad_personaje)
                    case "correr_izquierda":
                        if not self.esta_saltando:
                            self.animar_personaje(pantalla,"correr_izquierda")
                        self.mover_personaje(self.velocidad_personaje *-1)
                    case "saltar_derecha":
                        if not self.esta_saltando:
                            self.esta_saltando = True
                            self.desplazamiento_y = self.potencia_salto_personaje
                    case "quieto_derecha":
                        if not self.esta_saltando:
                            self.animar_personaje(pantalla,"quieto_derecha")
                self.aplicar_gravedad_personaje(pantalla,lista_plataformas)
                self.aplicar_colision_enemigo(pantalla,lista_enemigos)
                self.aplicar_colision_items(pantalla,lista_items)
        elif self.win:
            self.animar_personaje(pantalla,"quieto_derecha")
        elif self.muerto:
            self.animar_personaje(pantalla,"muerte")
        
