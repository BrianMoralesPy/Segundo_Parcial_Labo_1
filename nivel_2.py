from constantes import *
from ver_rectangulos import *
from items import Item
from personaje import Personaje
from plataformas import Plataforma
from enemigos import Enemigo
from configuraciones import *
from pygame.locals import *
from puntaje import *
import pygame,sys
def Nivel_2() -> None: #contiene todo el nivel 2
    
    pygame.init()
    pygame.display.set_caption('GAME')
    nombre_jugador = ""
    cuadro_texto_activo = False
    texto_nombre = ''
    input_box = pygame.Rect(300, 400, 140, 32)
    color_activo = NEGRO
    color = color_activo
    guardado = False
    
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
    fondo = pygame.image.load("imagenes/fondos/fondo_nivel_2.jpg")
    fondo = pygame.transform.scale(fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
    fuente = pygame.font.SysFont("Arial",50)
    fuente_2 = pygame.font.SysFont("Arial",25)
    texto_derrota = fuente.render('Game Over', True, (NEGRO))
    texto_victoria = fuente.render('You Win', True, (NEGRO))
    #MUSICA
    pygame.mixer.music.load("musica/Gundam Battle Assault MA-08 Big Zam theme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    
    reloj = pygame.time.Clock()
    #PERSONAJE
    
    #DICCIONARIO ANIMACIONES PERSONAJE
    diccionario_animaciones = {}
    diccionario_animaciones["quieto_derecha"] = lista_img__quieto_derecha
    diccionario_animaciones["saltar_derecha"] = lista_img_saltando_derecha
    diccionario_animaciones["saltar_izquierda"] = lista_img_saltando_izquierda
    diccionario_animaciones["correr_derecha"] = lista_img_derecha
    diccionario_animaciones["correr_izquierda"] = lista_img_izquierda
    diccionario_animaciones["recibir_daño"] = lista_img_recibir_daño
    diccionario_animaciones["muerte"] = lista_img_muerte
    personaje = Personaje((25,25),(2,434),diccionario_animaciones,7,30,5,5)

    #DICCIONARIO ANIMACIONES ENEMIGO
    diccionario_animaciones_enemigo = {}
    diccionario_animaciones_enemigo["correr_derecha"] = lista_enemigo_derecha_2
    diccionario_animaciones_enemigo["correr_izquierda"] = lista_enemigo_izquierda_2
    diccionario_animaciones_enemigo["recibir_daño"] = lista_enemigo_recibir_daño_2


    #ENEMIGOS
    enemigo_1 = Enemigo((50,50),(350,35),diccionario_animaciones_enemigo,550,4,6,1)
    enemigo_2 = Enemigo((50,50),(606,210),diccionario_animaciones_enemigo,765,4,6,1)
    enemigo_3 = Enemigo((50,50),(352,250),diccionario_animaciones_enemigo,530,4,6,1)
    enemigo_4 = Enemigo((50,50),(12,195),diccionario_animaciones_enemigo,185,4,6,1)
    lista_enemigos = [enemigo_1,enemigo_2,enemigo_3,enemigo_4]
    #PLATAFORMAS
    piso = Plataforma((800,50),(0,475),"imagenes\plataformas\piso_invisible.png")
    plataforma_1 = Plataforma((200,50),(4,241),"imagenes\plataformas\plataforma_1.png")
    plataforma_2 = Plataforma((200,50),(357,80),"imagenes\plataformas\plataforma_2.png")
    plataforma_3 = Plataforma((200,50),(600,256),"imagenes\plataformas\plataforma_1.png")
    plataforma_4 = Plataforma((200,50),(339,298),"imagenes\plataformas\plataforma_2.png")
    lista_plataformas = [piso,plataforma_1,plataforma_2,plataforma_3,plataforma_4]
    #ITEMS
    item_1 = Item((30,30),(136,164),"imagenes/items_nivel_2/carne_2.png")
    item_2 = Item((30,30),(375,242),"imagenes/items_nivel_2/carne_2.png")
    item_3 = Item((30,30),(534,44),"imagenes/items_nivel_2/carne_2.png")
    item_4 = Item((30,30),(660,188),"imagenes/items_nivel_2/carne_2.png")
    item_5 = Item((30,30),(639,410),"imagenes/items_nivel_2/carne_2.png")
    item_6 = Item((30,30),(242,372),"imagenes/items_nivel_2/carne_2.png")
    lista_items = [item_1,item_2,item_3,item_4,item_5,item_6] 
    ejecutar = True
    while ejecutar:
        reloj.tick(FPS) 
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            
            if evento.type == pygame.QUIT:
                ejecutar = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(f"coordenadas: x = {x} y = {y}")
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] and personaje.lados_personaje["main"].right < ANCHO_PANTALLA - personaje.velocidad_personaje):
            personaje.accion = 'correr_derecha'
        elif (keys[pygame.K_LEFT] and personaje.lados_personaje["main"].x > personaje.velocidad_personaje):
            personaje.accion = 'correr_izquierda'
        elif keys[pygame.K_SPACE]:
            personaje.accion = 'saltar_derecha'
        else:   
            personaje.accion = 'quieto_derecha'
        
        pantalla.blit(fondo,(0,0))
        personaje.update(pantalla,lista_plataformas,lista_enemigos,lista_items)
        
        for plataforma in lista_plataformas:
            plataforma.update(pantalla)
        
        for item in lista_items:
            item.update(pantalla)
        
        for enemigo in lista_enemigos:
            enemigo.update(pantalla,personaje)
        lista_enemigos = [enemigo for enemigo in lista_enemigos if not enemigo.esta_muerto()] #quita a los enemigos
        
        if personaje.vidas <= 0 or personaje.puntos >= 120:
            pygame.mixer.music.set_volume(0.0)

            if not cuadro_texto_activo:
                for evento in lista_eventos:
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            cuadro_texto_activo = True
            
            elif cuadro_texto_activo:
                for evento in lista_eventos:
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            if not guardado:
                                # Guarda el nombre en la variable 'nombre_jugador'
                                nombre_jugador = texto_nombre
                                print("Nombre ingresado:", nombre_jugador)
                                cuadro_texto_activo = False
                                texto_nombre = ''  # Limpia el texto después de presionar Enter
                                guardar_puntos_en_csv(nombre_jugador,personaje.puntos)
                                guardado = True
                        elif evento.key == pygame.K_BACKSPACE:
                            texto_nombre = texto_nombre[:-1]
                        else:
                            texto_nombre += evento.unicode
                                
                txt_surface = fuente_2.render(texto_nombre, True, color)
                width = max(200, txt_surface.get_width()+10)
                input_box.w = width
                pantalla.blit(txt_surface, (input_box.x+5, input_box.y+5))
                pygame.draw.rect(pantalla, color, input_box, 2)
        
        
        
        if personaje.vidas <= 0:
            pygame.mixer.music.set_volume(0.0)
            pantalla.blit(texto_derrota,(321,225))
        elif personaje.puntos >= 120:
            pygame.mixer.music.set_volume(0.0)
            pantalla.blit(texto_victoria,(321,225))
        
        if get_mode():
            for lado in personaje.lados_personaje:
                pygame.draw.rect(pantalla,"Orange",personaje.lados_personaje[lado], 2)
            for plataforma in lista_plataformas:
                for lado in plataforma.lados_plataforma:
                    pygame.draw.rect(pantalla,"Blue",plataforma.lados_plataforma[lado],2)
            for item in lista_items:
                for lado in item.lados_item:
                    pygame.draw.rect(pantalla,"Blue",item.lados_item[lado],2)
            for enemigo in lista_enemigos:
                for lado in enemigo.lados_enemigo:
                    pygame.draw.rect(pantalla,"Blue",enemigo.lados_enemigo[lado],2)
        pygame.display.update()