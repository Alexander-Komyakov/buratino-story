#!/usr/bin/env python3

import time, pygame, random, sys

pygame.init() #инициализируем pygame
display_width = pygame.display.Info().current_w
display_height = pygame.display.Info().current_h
class Player(): #игрок
    def __init__(self, x, y, path, stop, coord, name): #координаты x y путь к картинке, остановлен, координаты по цифрам, имя
        self.x = x; self.y = y
        self.path = path
        self.stop = stop
        self.coord = coord
        self.name = name
        self.sprite = pygame.image.load(path)

    def beginToEnd(self, endX, endY, speed=0.001): #двигает игрока к конечной точке на 1 пиксель и если он достиг возвращает True
        end = False
        if self.x + 50 >= endX - 5 and self.x + 50 <= endX + 5: #если равен конечной точке по X
            end = True
        elif self.x + 50 < endX: #если x игрока меньше конечной точки
            self.x += 4 #увеличиваем x игрока
        elif self.x + 50 > endX: #если x игрока больше
            self.x -= 4 #уменьшаем

        if self.y + 50 >= endY - 5 and  self.y + 50 <= endY + 5: #если пришел к концу по x и по y
            if end == True:
                return True #повзвращаем True
        elif self.y + 50 < endY:
            self.y += 4
        elif self.y + 50 > endY:
            self.y -= 4
        #time.sleep(speed)
        return False

class Menu():
    def __init__(self, punkts = [["Game", 16, 0, 0]]):
        self.punkts = punkts #массив данных о пунктах: текст размер x y
        self.numPunkt = 0 #выбранный номер пункта в меню
        #Выбираем шрифт, который мы будем использовать.
        #Стандартный шрифт, 25 точек.
        self.font = pygame.font.Font(None, 25) 

        #Рисуем текст. "True" означает использовать сглаживание
        #цвет текста. Следующая строка создает образ текста
        #но не рисует его на экране.
        self.text = self.font.render("My text", True, [0, 0, 0])
    def render(self, screen, Punkt, punkts):
        screen.fill((0, 0, 255))
        for i in punkts:
            if i == Punkt:
                self.font = pygame.font.Font(None, i[1]) 
                self.text = self.font.render(i[0], True, [255, 0, 0])
                screen.blit(self.text, (i[2], i[3]))
            else:
                self.font = pygame.font.Font(None, i[1]) 
                self.text = self.font.render(i[0], True, [0, 0, 0])
                screen.blit(self.text, (i[2], i[3]))
        pygame.display.update()
    def start(self, win):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        if self.numPunkt < len(punkts)-1:
                            self.numPunkt += 1
                    if event.key == pygame.K_UP:
                        if self.numPunkt >= 1:
                            self.numPunkt -= 1
                    if event.key == pygame.K_RETURN:
                        if self.numPunkt == 3:
                            sys.exit()
                        elif self.numPunkt == 0:
                            return 0
                        elif self.numPunkt == 1:
                            return 1
                        elif self.numPunkt == 2:
                            return 2

            self.render(win, punkts[self.numPunkt], self.punkts)
    def pause(self, win):
        punktsPause = [["Продолжить", 116, display_width//2 - 180, display_height//2 - 168],\
                ["Выход", 116, display_width//2 - 180, (display_height//2) - 68]]
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        if self.numPunkt < len(punkts)-3:
                            self.numPunkt += 1
                    if event.key == pygame.K_UP:
                        if self.numPunkt >= 1:
                            self.numPunkt -= 1
                    if event.key == pygame.K_RETURN:
                        if self.numPunkt == 1:
                            sys.exit()
                        elif self.numPunkt == 0:
                            return 0
            self.render(win, punktsPause[self.numPunkt], punktsPause)



def drawWindow(Gamers): #обновление окна и рисование на нем
    win.blit(fon, (0, 0))
    win.blit(cubSprite, (20, 20))
    for i in Gamers:
        win.blit(i.sprite, ((i.x * (display_width/1920)), (i.y * (display_height/1080))))

    pygame.display.update()

def CoordStop(coord): #наступил ли на останавливающую кнопку
    if coord == 6 or coord == 17 or coord == 25 or coord == 30 or coord == 43\
            or coord == 46 or coord == 49 or coord == 53 or coord == 57\
            or coord == 62 or coord == 71 or coord == 75 or coord == 89\
            or coord == 100:
        return True
    else:
        return False

def CoordCalculation(coord): #расчет координат героя
    #когда становится на оранжевую или голубую перемещается в какую-либо сторону
    if coord == 9:
        coord = 14
    elif coord == 16:
        coord = 18
    elif coord == 20:
        coord = 8
    elif coord == 26:
        coord = 30
    elif coord == 37:
        coord = 42
    elif coord == 44:
        coord = 24
    elif coord == 56:
        coord = 52
    elif coord == 59:
        coord = 41
    elif coord == 63:
        coord = 66
    elif coord == 69:
        coord = 65
    elif coord == 81:
        coord = 85
    elif coord == 87:
        coord = 55
    elif coord == 94:
        coord = 79
    return coord

#координаты по которым ставим модельки игроков (x;y) 1 - 100 
coordMap = [[1748, 950], [1660, 945], [1570, 965], [1453, 968], [1359, 965],\
        [1272, 957], [1170, 956], [1076, 956], [986, 960],\
        [892, 964], [820, 957], [751, 951], [631, 964],\
        [487, 948], [405, 948], [304, 952], [188, 966],\
        [101, 920], [297, 792], [426, 805], [518, 822],\
        [618, 830], [713, 820], [840, 805], [936, 797],\
        [1055, 800], [1151, 803], [1253, 813], [1340, 821],\
        [1418, 825], [1552, 795], [1667, 831], [1771, 793],\
        [1789, 733], [1763, 671], [1701, 630], [1572, 620],\
        [1471, 625], [1385, 640], [1295, 652], [1206, 651],\
        [1190, 636], [1017, 617], [925, 647], [818, 657],\
        [623, 669], [498, 669], [382, 676], [237, 660],\
        [136, 627], [113, 571], [155, 524], [222, 487],\
        [311, 472], [400, 483], [541, 510], [639, 509],\
        [753, 482], [859, 448], [980, 411], [1089, 458],\
        [1133, 507], [1212, 527], [1500, 512], [1584, 502],\
        [1664, 497], [1767, 495], [1806, 365], [1740, 343],\
        [1628, 350], [1528, 362], [1398, 405], [1309, 419],\
        [1231, 417], [1160, 408], [1217, 355], [1150, 331],\
        [1087, 309], [982, 313], [882, 339], [818, 359],\
        [689, 376], [609, 381], [531, 384], [453, 381],\
        [371, 377], [305, 353], [224, 343], [122, 286],\
        [263, 232], [370, 239], [451, 240], [531, 242],\
        [606, 251], [690, 242], [795, 207], [867, 226],\
        [942, 243], [1012, 243], [1088, 235], [1178, 206]]


pygame.display.toggle_fullscreen #полноэкранный режим
win = pygame.display.set_mode((display_width, display_height)) #создаем окно
pygame.display.set_caption("Buratino Story") #подписываем окно
fon = pygame.image.load("fon.jpeg") #загружаем карту игры
fon = pygame.transform.scale(fon, (display_width, display_height))
cubSprite = pygame.image.load("kost1.png") #спрайт кубика

#пункты меню
punkts = [["Два игрока", 116, display_width//2 - 180, display_height//2 - 168],\
        ["Три игрока", 116, display_width//2 - 180, (display_height//2) - 68],\
        ["Четыре игрока", 116, display_width//2 - 180, (display_height//2) + 32],\
        ["Выход", 116, display_width//2 - 180, (display_height//2) + 132]]

menu = Menu(punkts) #создаем объект класса Menu

#создаем игроков
Gamers = [Player(1692, 900, "player1.png", 0, 0, "1"),\
        Player(1718, 900, "player2.png", 0, 0, "2")]

item_selection = menu.start(win) #возвращает выбранный пункт меню
if item_selection == 1: #если игрок выбрал игроку в троем
    Gamers.append(Player(1649, 896, "player3.png", 0, 0, "3"))
elif item_selection == 2: #если выбрал игроку в четвером
    Gamers.append(Player(1649, 896, "player3.png", 0, 0, "3"))
    Gamers.append(Player(1670, 896, "player4.png", 0, 0, "4"))

drawWindow(Gamers) #рисуем фон

victory = False #победа
move = 0

vicText = pygame.font.Font(None, 100) 
text = vicText.render("Победил ", True, [255, 0, 0])

while victory == False: #пока никто не победил работает игра
 
    drawWindow(Gamers)

    if CoordStop(Gamers[move].coord): #если герой стоит на красной кнопке
        if Gamers[move].stop == 1: #пропустил ли он уже один ход
            Gamers[move].stop = 0 #продолжает игру
        else: #если еще не пропустил
            Gamers[move].stop = 1 #пропускает
    else: #если он не на красной
        Gamers[move].stop = 0 #убираем остановку героя

    if Gamers[move].stop == 1: #если игрок наступил на красную
        if move < len(Gamers)-1: #передаем ход следующему игроку
            move += 1
        else: #если последний игрок
            move = 0 #передаем ход первому игроку
        Gamers[move].stop = 0 #обнуляем его остановку
    
    #бросок кубика
    key = True #нажал ли игрок клавишу
    #управление
    while key:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    key = False 
                if event.key == pygame.K_ESCAPE:
                    menu.pause(win)
                    drawWindow(Gamers)
                    
    cub = random.randint(1, 6)
    pathToCub = str("kost"+str(cub)+".png")
    cubSprite = pygame.image.load(pathToCub) #спрайт кубика
    #print(Gamers[move].name, "выпало число", cub)
    #проверяем, не победил ли кто-то
    for i in range(0, len(Gamers)):
        if Gamers[i].coord > 100:
            drawWindow(Gamers)
            text = vicText.render("Победил "+Gamers[i].name+" игрок", True, [255, 0, 0])
            win.blit(text, (650 * (display_width/1920), 500 * (display_height/1080)))
            pygame.display.update()
            time.sleep(3)
            sys.exit()

    if Gamers[move].coord + cub > 100 or CoordCalculation(Gamers[move].coord + cub) > 100:
        drawWindow(Gamers)
        text = vicText.render("Победил "+Gamers[i].name+" игрок", True, [255, 0, 0])
        win.blit(text, (650, 500))
        pygame.display.update()
        time.sleep(3)
        sys.exit()


    #плавное движение модельки к месту
    begin = Gamers[move].coord #начальная координата героя
    end = Gamers[move].coord + cub #конечная требуемая координата
    for i in range(begin, end): #двигаем игрока по одной точке
        while True:
            if i + 1 <= end and Gamers[move].beginToEnd(coordMap[i+1][0], coordMap[i+1][1]): #если игрок пришел к требуемой точке
                #и она не предпоследняя
                break #переходим к следующей
            drawWindow(Gamers) #обновляем экран

    
    Gamers[move].coord += cub #прибавляем к координатам героя число выпавшее

    #плавное движение модельки к месту
    begin = Gamers[move].coord #начальная координата героя
    end = CoordCalculation(Gamers[move].coord) #конечная требуемая координата
    while True:
        if Gamers[move].beginToEnd(coordMap[end][0], coordMap[end][1]): #если игрок пришел к требуемой точке
            break #переходим к следующей
        drawWindow(Gamers) #обновляем экран

    Gamers[move].coord = CoordCalculation(Gamers[move].coord) #расчитываем координаты игрока

    if Gamers[move].coord != 90: #если игрок не стоит на зеленой кнопке
        if move < len(Gamers)-1: #передаем ход следующему игроку
            move += 1
        else: #если последний игрок
            move = 0 #передаем ход первому игроку
    
    #ставим фигурки на позиции
    for i in range(0, len(Gamers)):
        Gamers[i].x = coordMap[Gamers[i].coord][0] - 50 
        Gamers[i].y = coordMap[Gamers[i].coord][1] - 50 

