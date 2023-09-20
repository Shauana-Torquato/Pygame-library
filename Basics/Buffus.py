#criaöäao da janela
#importanto a biblioteca pygame e submodolo para as constantes e funcoes que serao utiliyadas no script

import pygame
from pygame.locals import *

#importar funöäao que estüa dentro so modo sys e que serve para fechar a janela

from sys import exit

# comecando o script de fato, inicialiyar todas as funöoes e variaveis da biblioteca pzgame

pygame.init()

# criar o objeto que serü a tela definindo a altura e largura que esta tela irüa ter

largura = 640
altura = 480

tela = pygame.display.set_mode (largura, altura)

# tem que ser criado um loop principal do jogo, que vem a ser um loop infinito, pois a cada segundo que vocÖe estüa jogando, este jogo deve ser atualiyado. e todo oscript do jogo deve estar dentro deste loop principal

while True:

# um novo loop deve ser criado dentro do loop principal e esse loop for vai ter a tarefa de a cada interaöäo do loop principal, ele irüa verificar e detectar se algum evento ocorreu e em atendendo uma condiöäao, farüa algo

    for event in pygame.event.get():
        