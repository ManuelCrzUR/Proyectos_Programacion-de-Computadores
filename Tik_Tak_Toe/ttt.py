# Se importan los paquetes y librerias necesarios para el proyecto
from turtle import width
import pygame
import sys
import time
from pygame.locals import *

#       DECLARANDO VARIABLES DE USO GENERAL     #

#   Variables necesarias para la ventana:
width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)

#   Para guardar juego:
XO = "x"

#   Condicionales de resultados:
winner = None
draw = None

#   Organizando tablero 3 x 3:
board = [[None] * 3, [None] * 3, [None] * 3]

# Se inicializa el paquete de pygame y el registro del tiempo
pygame.init()
clock = pygame.time.Clock()

# Se construye la base de la pagina y un tag
screen = pygame.display.set_mode((width, height + 100), 0, 32)
pygame.display.set_caption("Tic-Tac-Toe | Proyecto")

# Cargando imagenes: -- Falta la x y o
initiating_window = pygame.image.load("carga_ttt.jpg")

# Funcion la cual construye la ventana de juego
def abrir_ventana():
    screen.blit(initiating_window, (0, 0))
    
    pygame.display.update()
    time.sleep(3)
    screen.fill(white)
    
    pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    
    pygame.draw.line(screen, line_color, (0, height / 3,), (width, height / 3), 7)
    pygame.draw.line(screen, line_color, (0, height / 3 * 2,), (width, height / 3), 7)
    draw_status()
    
def draw_status():
    # Añadiendo accion despues de algun reusltado
    global draw
    
    if winner is None:
        message = "Turno de " + XO.upper()
    else:
        message = winner.upper() + "ganó !"
        
    if draw:
        message = "Es un empate !"
    
abrir_ventana()