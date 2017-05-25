from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from GameState import*
from Frame import *

#Geral
janela = Window(700, 400)
janela.set_title("Make America a Game Again")
teclado = Window.get_keyboard()
status=GameState(GameState.START)

# Botao de Start
fundo_start = GameImage("Again.png")
button_start = Sprite("Start.png", 2)
button_start.set_total_duration(1000)
button_start.move_x(108)
button_start.move_y(324)
button_start.set_sequence(0, 2,True)

# Tela inicial
status_escolhas = Frame(Frame.JOGAR)
fundo_escolhas = GameImage("Flag.jpg")
frame_escolhas = GameImage("Frame.png")

# Jogo



def start(teclado):
    fundo_start.draw()
    button_start.draw()
    button_start.update()
    if(teclado.key_pressed("SPACE")):
            status.setState(GameState.ESCOLHAS)

def escolhas(teclado):
    fundo_escolhas.draw()
    frame_escolhas.draw()

    if ((teclado.key_pressed("w")) or (teclado.key_pressed("up"))) and status_escolhas.getState()== 1:
        status_escolhas.setState(Frame.SAIR)
        janela.delay(150)
    elif ((teclado.key_pressed("s")) or (teclado.key_pressed("down"))) and status_escolhas.getState()== 1:
        status_escolhas.setState(Frame.CONTROLES)
        janela.delay(150)
    elif ((teclado.key_pressed("w")) or (teclado.key_pressed("up"))) and status_escolhas.getState()== 2:
        status_escolhas.setState(Frame.JOGAR)
        janela.delay(150)
    elif ((teclado.key_pressed("s")) or (teclado.key_pressed("down"))) and status_escolhas.getState()== 2:
        status_escolhas.setState(Frame.SAIR)
        janela.delay(150)
    elif ((teclado.key_pressed("w")) or (teclado.key_pressed("up"))) and status_escolhas.getState()== 3:
        status_escolhas.setState(Frame.CONTROLES)
        janela.delay(150)
    elif ((teclado.key_pressed("s")) or (teclado.key_pressed("down"))) and status_escolhas.getState()== 3:
        status_escolhas.setState(Frame.JOGAR)
        janela.delay(150)

    if status_escolhas.getState() == 1:
        frame_escolhas.set_position(256,125)
        if teclado.key_pressed("ENTER"):
            status.setState(GameState.JOGO)
    elif status_escolhas.getState() == 2:
        frame_escolhas.set_position(256,201)
        if teclado.key_pressed("ENTER"):
            print("AINDA NAO IMPLEMENTADO!")
    elif status_escolhas.getState() == 3:
        frame_escolhas.set_position(256,282)
        if teclado.key_pressed("ENTER"):
            janela.close()

def personagem():
    print("AINDA NAO IMPLEMENTADO")

def jogo():
    print("Coloca o jogo aqui POVO ")



while True:
    if status.getState() == GameState.START:
        start(teclado)
    elif status.getState() == GameState.ESCOLHAS:
        escolhas(teclado)
    elif status.getState() == GameState.PERSONAGEM:
        personagem()
    elif status.getState() == GameState.JOGO:
        jogo()
    janela.update()
