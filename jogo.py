from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *

janela = Window(528, 316)
fundo = GameImage("background.jpg")
w = fundo.width
h = fundo.height

fundo.set_position(0, 0)
print("w=",w, "h=",h)

janela.set_title("03")
animacao = Sprite("full.png", 37)
animacao2 = Sprite("full2.png", 37)
hp = Sprite('hp.png', 11)
hp2 = Sprite('hp2.png', 11)


animacao.set_total_duration(3000)
animacao2.set_total_duration(3000)
hp.set_total_duration(11000)
hp2.set_total_duration(11000)

animacao.move_x(528 - 520)
animacao.move_y(316 - 120)

hp.move_x(20)
hp.move_y(30)
hp2.move_x(345)
hp2.move_y(30)

animacao2.move_x(528 - 60)
animacao2.move_y(316 - 120)


teclado = Window.get_keyboard()

attack1 = 0
attack2 = 0
dist1 = 0
dist2 = 4700
jump = 0
altura = 0
sentido = 'w'
animacao.set_sequence(7, 18, True)
sentido2 = 'w'
animacao2.set_sequence(18, 29, True)


while(True):

    if(teclado.key_pressed("A")):
        if (sentido != 'L' and altura == 0):
            animacao.set_sequence(19, 27, True)
        sentido = 'L'
        if dist1>0 and lockmove ==0:
            animacao.move_x(-0.1)
            dist1 = dist1 - 1

    elif(teclado.key_pressed("D")):
        if (sentido != 'R' and altura == 0):
            animacao.set_sequence(28, 37, True)
        sentido = 'R'
        if dist1<4700 and lockmove ==0:
            animacao.move_x(0.1)
            dist1 = dist1 + 1

    else:
        if sentido != 'w':
            animacao.set_sequence(7, 18, True)
        sentido = 'w'

    if(teclado.key_pressed("f")):
        attack1 = 1
    else:
        attack1 = 0




    if(teclado.key_pressed("left")):
        if (sentido2 != 'L' and altura == 0):
            animacao2.set_sequence(9, 17, True)
        sentido2 = 'L'
        if dist2>0 and lockmove ==0:
            animacao2.move_x(-0.1)
            dist2 = dist2 - 1

    elif(teclado.key_pressed("right")):
        if (sentido2 != 'R' and altura == 0):
            animacao2.set_sequence(0, 8, True)
        sentido2 = 'R'
        if dist2<4700 and lockmove ==0:
            animacao2.move_x(0.1)
            dist2 = dist2 + 1

    else:
        if sentido2 != 'w':
            animacao2.set_sequence(18, 29, True)
        sentido2 = 'w'

    if (teclado.key_pressed("L")):
        attack2 = 1
    else:
        attack2 = 0



    if (animacao.collided(animacao2)):
        animacao.move_x(-0.0002)
        animacao2.move_x(0.0002)
        lockmove = 1
    else:
        lockmove = 0

    if dist2-dist1<680:
        if attack2 == 1:
            hp.update()
        if attack1 == 1:
            hp2.update()

    print(dist2-dist1)





    ###################PULO################
    #if(teclado.key_pressed("up")):
    #    if jump != 0:
    #        animacao.set_sequence(0, 6, True)
    #    jump = 2
    #    sentido = 'w'
    #if jump == 2 and altura<800:
    #    animacao.move_y(-0.14)
    #    altura = altura + 1
    #if altura >=800:
    #    jump = 1
    #if jump == 1 and altura>0:
    #    altura = altura -1
    #    animacao.move_y(0.14)
    #if altura == 0:
    #    jump = 0
    ###################PULO##############
    fundo.draw()
    hp2.draw()
    hp.draw()
    animacao.draw()
    animacao2.draw()
    animacao.update()
    animacao2.update()

    janela.update()

