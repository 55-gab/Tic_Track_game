#pgzero
import random

WIDTH = 820
HEIGHT = 600

TITLE = "Tic track"
FPS = 30

cars_owned= {"haas": False, "astonm": False, "ferrari": False, "mclaren": False}

background_menu = Actor("menu")
menu1 = Actor("menu", (WIDTH/2, 0))
menu2 = Actor("menu", (WIDTH/2, -HEIGHT))

titulo = Actor("tictrack", (420,130))
start = Actor("start", (430,260))
store = Actor("store", (430,380))
garage = Actor("garage", (420,510))

background_nivel1 = Actor("nivel1")
nivel1_1 = Actor("nivel1", (WIDTH/2, 0))
nivel1_2 = Actor("nivel1", (WIDTH/2, -HEIGHT))
car_n = Actor("williams",(580,460))

background_nivel2 = Actor("nivel2")
nivel2_1 = Actor("nivel2", (WIDTH/2, 0))
nivel2_2 = Actor("nivel2", (WIDTH/2, -HEIGHT))

background_nivel3 = Actor("nivel3")
nivel3_1 = Actor("nivel3", (WIDTH/2, 0))
nivel3_2 = Actor("nivel3", (WIDTH/2, -HEIGHT))

rivales_creados = 0
rivals = []

x = random.randint(350, 492)
y = random.randint(-650, -50)
rival = Actor("rival", (x,y))
rival.speed = random.randint(5, 8)
rival.pasado = False
rivals.append(rival)
rivales_creados += 1

fondo_b = Actor("fondo_b")
bandera1 = Actor("fondo_b", (WIDTH/2, 0))
bandera2 = Actor("fondo_b", (WIDTH/2, -HEIGHT))
trofeo = Actor("trofeo")

boton_menu = Actor("boton_menu",(710,55))
boton_menu1 = Actor("boton_menu",(650,530))
boton_menu_n = Actor("boton_menu",(240,470))
boton_next = Actor("next",(580,470))
boton_next2 = Actor("next",(580,470))

store_f = Actor("store_fondo")
haas = Actor("haas",(135,180))
aston = Actor("astonm",(305,425))
ferrari = Actor("ferrari",(500,180))
mclaren = Actor("mclaren",(700,430))
boton_storeh = Actor("boton_store",(305,180))
boton_storea = Actor("boton_store",(135,425))
boton_storef = Actor("boton_store",(700,180))
boton_storem = Actor("boton_store",(500,430))

garage_f = Actor("garage_fondo")
car_d1 = Actor("car_d",(150,150))
car_d2 = Actor("car_d",(370,150))
car_d3 = Actor("car_d",(150,440))
car_d4 = Actor("car_d",(370,440))
williams = Actor("williams",(640,290))

nivel_actual = 1
niveles_r = {1: 5, 2: 10, 3: 20}
rivales_max = niveles_r[nivel_actual]
partida_f = False
pts = 0
coins = 5000
scroll_speed = 3
mode = 'menu_p'

def draw():
    if mode == "menu_p":
        background_menu.draw()
        menu1.draw()
        menu2.draw()
        titulo.draw()
        start.draw()
        store.draw()
        garage.draw()

    elif mode == "nivel1":
        background_nivel1.draw()
        nivel1_1.draw()
        nivel1_2.draw()
        screen.draw.text("pts:" + str(pts),center = (70,52),color = "white",fontsize = 62)
        screen.draw.text("pts:" + str(pts),center = (70,50),color = "black",fontsize = 60)

        screen.draw.text("$:" + str(coins),center = (70,92),color = "white",fontsize = 62)
        screen.draw.text("$:" + str(coins),center = (70,90),color = "black",fontsize = 60)

        car_n.draw()
        for i in range(len(rivals)):
         rivals[i].draw()

    elif mode == "nivel2":
        background_nivel2.draw()
        nivel2_1.draw()
        nivel2_2.draw()
        screen.draw.text("pts:" + str(pts),center = (70,52),color = "white",fontsize = 62)
        screen.draw.text("pts:" + str(pts),center = (70,50),color = "black",fontsize = 60)

        screen.draw.text("$:" + str(coins),center = (70,92),color = "white",fontsize = 62)
        screen.draw.text("$:" + str(coins),center = (70,90),color = "black",fontsize = 60)

        car_n.draw()
        for i in range(len(rivals)):
         rivals[i].draw()

    elif mode == "nivel3":
        background_nivel3.draw()
        nivel3_1.draw()
        nivel3_2.draw()
        screen.draw.text("pts:" + str(pts),center = (70,52),color = "white",fontsize = 62)
        screen.draw.text("pts:" + str(pts),center = (70,50),color = "black",fontsize = 60)

        screen.draw.text("$:" + str(coins),center = (70,92),color = "white",fontsize = 62)
        screen.draw.text("$:" + str(coins),center = (70,90),color = "black",fontsize = 60)

        car_n.draw()
        for i in range(len(rivals)):
         rivals[i].draw()

    elif mode == "intermission":
        fondo_b.draw()
        bandera1.draw()
        bandera2.draw()
        trofeo.draw()
        boton_menu_n.draw()
        boton_next.draw()

    elif mode == "intermission2":
        fondo_b.draw()
        bandera1.draw()
        bandera2.draw()
        trofeo.draw()
        boton_menu_n.draw()
        boton_next2.draw()

    elif mode == "final":
        fondo_b.draw()
        bandera1.draw()
        bandera2.draw()
        trofeo.draw()
        boton_menu_n.draw()


    elif mode == "store_p":
        store_f.draw()
        boton_menu.draw()
        haas.draw()
        aston.draw()
        ferrari.draw()
        mclaren.draw()
        boton_storeh.draw()
        screen.draw.text("20coins",center = (305,180),color = "black",fontsize = 55)
        boton_storea.draw()
        screen.draw.text("30coins",center = (135,425),color = "black",fontsize = 55)
        boton_storef.draw()
        screen.draw.text("50coins",center = (700,180),color = "black",fontsize = 55)
        boton_storem.draw()
        screen.draw.text("40coins",center = (500,430),color = "black",fontsize = 55)



    elif mode == "garage_p":
        garage_f.draw()
        boton_menu1.draw()
        car_d1.draw()
        car_d2.draw()
        car_d3.draw()
        car_d4.draw()
        if cars_owned["haas"]:
            car_d1.image = "haas"
        else:
            car_d1.image = "car_d"

        if cars_owned["astonm"]:
            car_d2.image = "astonm"
        else:
            car_d2.image = "car_d"

        if cars_owned["ferrari"]:
            car_d3.image = "ferrari"
        else:
            car_d3.image = "car_d"

        if cars_owned["mclaren"]:
            car_d4.image = "mclaren"
        else:
            car_d4.image = "car_d"

        if cars_owned["mclaren"]:
            car_d4.image = "mclaren"
        else:
            car_d4.image = "car_d"

        williams.draw()

def new_rival():
    global rivales_creados, rivales_max
    if rivales_creados < rivales_max:
        x = random.randint(350, 492)
        y = -50
        rival = Actor("rival", (x, y))
        rival.speed = random.randint(5, 8)
        rival.pasado = False
        rivals.append(rival)
        rivales_creados += 1

def rival_car():
    for i in range(len(rivals) - 1, -1, -1):
        if rivals[i].y < 710:
            rivals[i].y += rivals[i].speed
        else:
            rivals.pop(i)
            new_rival()


def mover_fondo():
    global mode
    global menu1, menu2
    global nivel1_1,nivel1_2
    global nivel2_1, nivel2_2
    global nivel3_1, nivel3_2
    global bandera1,bandera2
    if mode == "menu_p":
        img_h = menu1.height

        menu1.y += scroll_speed
        menu2.y += scroll_speed

        # Si la parte superior de la pista salió por debajo de la pantalla:
        # top = pista.y - img_h/2
        if (menu1.y - img_h/2) >= HEIGHT:
            # colocar menu1 exactamente arriba de menu2
            menu1.y = menu2.y - img_h

        if (menu2.y - img_h/2) >= HEIGHT:
            menu2.y = menu1.y - img_h

    elif mode == "nivel1":
        img_h = nivel1_1.height

        nivel1_1.y += scroll_speed
        nivel1_2.y += scroll_speed

        if (nivel1_1.y - img_h/2) >= HEIGHT:
            nivel1_1.y = nivel1_2.y - img_h

        if (nivel1_2.y - img_h/2) >= HEIGHT:
            nivel1_2.y = nivel1_1.y - img_h

    elif mode == "nivel2":
        img_h = nivel2_1.height

        nivel2_1.y += scroll_speed
        nivel2_2.y += scroll_speed

        if (nivel2_1.y - img_h/2) >= HEIGHT:
            nivel2_1.y = nivel2_2.y - img_h

        if (nivel2_2.y - img_h/2) >= HEIGHT:
            nivel2_2.y = nivel2_1.y - img_h

    elif mode == "nivel3":
        img_h = nivel3_1.height

        nivel3_1.y += scroll_speed
        nivel3_2.y += scroll_speed

        if (nivel3_1.y - img_h/2) >= HEIGHT:
            nivel3_1.y = nivel3_2.y - img_h

        if (nivel3_2.y - img_h/2) >= HEIGHT:
            nivel3_2.y = nivel3_1.y - img_h

    elif mode == "intermission" or mode == "intermission2" or mode == "final":
        img_h = bandera1.height

        bandera1.y += scroll_speed
        bandera2.y += scroll_speed

        if (bandera1.y - img_h/2) >= HEIGHT:
            bandera1.y = bandera2.y - img_h

        if (bandera2.y - img_h/2) >= HEIGHT:
            bandera2.y = bandera1.y - img_h


def on_mouse_down(button, pos):
    global mode, pts, nivel_actual, coins
    if button == mouse.LEFT:
        if mode == "menu_p":
            if start.collidepoint(pos):
                mode = "nivel1"
            elif store.collidepoint(pos):
                mode = "store_p"
            elif garage.collidepoint(pos):
                mode = "garage_p"

        elif mode == "intermission":
            if boton_next.collidepoint(pos):
                nivel_actual = 2
                reiniciar()
                reset_fondos()
                mode = "nivel2"
            elif boton_menu_n.collidepoint(pos):
                mode = "menu_p"

        elif mode == "intermission2":
            if boton_next2.collidepoint(pos):
                nivel_actual = 3
                reiniciar()
                reset_fondos()
                mode = "nivel3"

            elif boton_menu_n.collidepoint(pos):
                mode = "menu_p"

        elif mode == "final":
            if boton_menu_n.collidepoint(pos):
                mode = "menu_p"

        elif mode == "store_p":
            if boton_menu.collidepoint(pos):
                mode = "menu_p"

            elif boton_storeh.collidepoint(pos) and coins >= 20 and not cars_owned["haas"]:
                cars_owned["haas"] = True
                car_n.image = "haas"
                coins -= 20


            elif boton_storea.collidepoint(pos) and coins >= 30 and not cars_owned["astonm"]:
                cars_owned["astonm"] = True
                car_n.image = "astonm"
                coins -= 30

            elif boton_storef.collidepoint(pos) and coins >= 40 and not cars_owned["ferrari"]:
                cars_owned["ferrari"] = True
                car_n.image = "ferrari"
                coins -= 40

            elif boton_storem.collidepoint(pos) and coins >= 50 and not cars_owned["mclaren"]:
                cars_owned["mclaren"] = True
                car_n.image = "mclaren"
                coins -= 50

        elif mode == "garage_p":
            if boton_menu1.collidepoint(pos):
                mode = "menu_p"
            elif car_d1.collidepoint(pos) and cars_owned["haas"]:
                car_n.image = "haas"

            elif car_d2.collidepoint(pos) and cars_owned["astonm"]:
                car_n.image = "astonm"

            elif car_d3.collidepoint(pos) and cars_owned["ferrari"]:
                car_n.image = "ferrari"

            elif car_d4.collidepoint(pos) and cars_owned["mclaren"]:
                car_n.image = "mclaren"

            elif williams.collidepoint(pos):
                car_n.image = "williams"




def on_key_down(key):
    global nivel_actual,mode

    if mode == "intermission":
        nivel_actual = 2
        reset_fondos()
        reiniciar()
        mode = "nivel2"

    elif mode == "intermission2":
        nivel_actual = 3
        reset_fondos()
        reiniciar()
        mode = "nivel3"

def reiniciar():
    global pts, rivales_max, rivales_creados, rivals, mode, partida_f

    pts = 0
    rivales_creados = 0
    partida_f = False
    rivals.clear()

    rivales_max = niveles_r[nivel_actual]

    x = random.randint(350, 492)
    y = -50
    rival = Actor("rival", (x,y))
    rival.speed = random.randint(5, 8)
    rival.pasado = False
    rivals.append(rival)
    rivales_creados += 1

def reset_fondos():
    menu1.pos = (WIDTH/2, 0)
    menu2.pos = (WIDTH/2, -HEIGHT)

    nivel1_1.pos = (WIDTH/2, 0)
    nivel1_2.pos = (WIDTH/2, -HEIGHT)

    nivel2_1.pos = (WIDTH/2, 0)
    nivel2_2.pos = (WIDTH/2, -HEIGHT)

    nivel3_1.pos = (WIDTH/2, 0)
    nivel3_2.pos = (WIDTH/2, -HEIGHT)

    bandera1.pos = (WIDTH/2, 0)
    bandera2.pos = (WIDTH/2, -HEIGHT)


def collisions():
    global mode
    for rival in rivals:
        if car_n.colliderect(rival):
            reset_fondos()
            reiniciar()
            mode = 'menu_p'
            reiniciar()
            return


def update():
    global pts, partida_f, mode, coins

    if mode in ("menu_p", "nivel1", "nivel2", "nivel3","intermission", "intermission2", "final"):
        mover_fondo()

    if mode in ("nivel1", "nivel2", "nivel3"):
        rival_car()
        collisions()

        if keyboard.up:
            car_n.y -= 5
        elif keyboard.down:
            car_n.y += 5
        elif keyboard.right:
            car_n.x += 5
        elif keyboard.left:
            car_n.x -= 5

        if not partida_f:
            for rival in rivals:
                if car_n.y < rival.y and not rival.pasado:
                    pts += 1
                    coins += 1
                    rival.pasado = True

            if pts >= rivales_max:
                partida_f = True
                if nivel_actual == 1:
                    mode = "intermission"
                elif nivel_actual == 2:
                    mode = "intermission2"
                elif nivel_actual == 3:
                    mode = "final"
