#!/usr/bin/env python3

import pygame
import random
import sys

class Menu():
    def __init__(self, punkts = [["Game", 16, 0, 0]]):
        self.punkts = punkts #массив данных о пунктах: текст размер x y
        self.numPunkt = 0 #выбранный номер пункта в меню
        # Выбираем шрифт, который мы будем использовать.
        # Стандартный шрифт, 25 точек.
        self.font = pygame.font.Font(None, 25) 

        # Рисуем текст. "True" означает использовать сглаживание
        # Black -- цвет текста. Следующая строка создает образ текста
        # но не рисует его на экране.
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
        punktsPause = [["Продолжить", 116, 1920//2 - 180, 1080//2 - 168],\
                ["Выход", 116, 1920//2 - 180, (1080//2) - 68]]
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
                        if self.numPunkt == 1:
                            sys.exit()
                        elif self.numPunkt == 0:
                            return 0
            self.render(win, punktsPause[self.numPunkt], punktsPause)



def drawWindow(): #обновление окна и рисование на нем
    win.blit(fon, (0, 0))
    win.blit(player1, (x1, y1))
    win.blit(player2, (x2, y2))
    win.blit(player3, (x3, y3))
    win.blit(player4, (x4, y4))

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
pygame.init() #инициализируем pygame
pygame.font.init() #инициализация шрифтов

win = pygame.display.set_mode((1920, 1080)) #создаем окно
pygame.display.set_caption("Buratino Story") #подписываем окно
fon = pygame.image.load("fon.jpeg") #загружаем карту игры

punkts = [["Два игрока", 116, 1920//2 - 180, 1080//2 - 168],\
        ["Три игрока", 116, 1920//2 - 180, (1080//2) - 68],\
        ["Четыре игрока", 116, 1920//2 - 180, (1080//2) + 32],\
        ["Выход", 116, 1920//2 - 180, (1080//2) + 132]]

menu = Menu(punkts) #создаем объект класса Menu
if menu.start(win) == 0:
    players = 2
elif menu.start(win) == 1:
    players = 3
elif menu.start(win) == 2:
    players = 4

#загружаем спрайты игроков
player1 = pygame.image.load("player1.png")
player2 = pygame.image.load("player2.png")
player3 = pygame.image.load("player3.png")
player4 = pygame.image.load("player4.png")

#ставим начальные координаты игроков
x1 = 1748 - (player1.get_width()//2) 
y1 = 950 - (player1.get_height()//2) 
x2 = 1768 - (player2.get_width()//2) 
y2 = 950 - (player2.get_height()//2) 

#третего и четвертого игрока может не быть, поэтому выводим сначала их за карту
x3 = -1000
y3 = -1000
x4 = -1000
y4 = -1000

drawWindow() #рисуем фон

#players = int(input("Введите кол-во игроков: ")) #кол-во игроков

#расставляем остальные фигурки в зависимости от кол-во игроков
if players == 3:
    x3 = 1699 - (player3.get_width()//2) 
    y3 = 944 - (player3.get_height()//2) 
if players >= 4: 
    x4 = 1720 - (player4.get_width()//2) 
    y4 = 944 - (player4.get_height()//2) 
    x3 = 1699 - (player3.get_width()//2) 
    y3 = 944 - (player3.get_height()//2) 
 
names = [] #имена игроков
coord = [] #координаты игроков
stop = [] #наступил ли герой на остановку(красную) move = 0 #номер игрока который ходит
victory = False #победа
move = 0

for i in range(0, players): #ввод имен игроков
    print("Введите имя", i+1, "игрока:", end=" ")
    names.append(str(i)) #вводим имя игрока
    coord.append(0) #добавляем начальную координату нового игрока
    stop.append(0) #обнуляем остановку героя

while victory == False: #пока никто не победил работает игра
    drawWindow()
    #отображение координат
    for i in range(0, players):
        print(names[i], coord[i])

    if CoordStop(coord[move]): #если герой стоит на красной кнопке
        if stop[move] == 1: #пропустил ли он уже один ход
            stop[move] = 0 #продолжает игру
        else: #если еще не пропустил
            stop[move] = 1 #пропускает
    else: #если он не на красной
        stop[move] = 0  #убираем остановку героя

    if stop[move] == 1: #если игрок наступил на красную
        if move < players-1: #передаем ход следующему игроку
            move += 1
        else: #если последний игрок
            move = 0 #передаем ход первому игроку
        stop[move] = 0 #обнуляем его остановку
    
    #бросок кубика
    print("Для броска кубика нажмите Enter")
    key = True #нажал ли игрок клавишу
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
                    drawWindow()
                    
    cub = random.randint(1, 6)
    print(names[move], "выпало число", cub)

    coord[move] += cub #прибавляем к координатам героя число выпавшее
    coord[move] = CoordCalculation(coord[move]) #расчитываем координаты игрока
    
    if coord[move] != 90: #если игрок не стоит на зеленой кнопке
        if move < players-1: #передаем ход следующему игроку
            move += 1
        else: #если последний игрок
            move = 0 #передаем ход первому игроку


    #проверяем, не победил ли кто-то
    for i in range(0, players):
        if coord[i] > 100:
            print("Победил(а)", names[i])
            input()
            victory = True

    #ставим фигурки на позиции
    if players == 2 and victory == False:
        x1 = coordMap[coord[0]][0] - (player1.get_width()//2) 
        y1 = coordMap[coord[0]][1] - (player1.get_height()//2) 
        x2 = coordMap[coord[1]][0] - (player2.get_width()//2) 
        y2 = coordMap[coord[1]][1] - (player2.get_height()//2) 
    elif players == 3 and victory == False:
        x1 = coordMap[coord[0]][0] - (player1.get_width()//2) 
        y1 = coordMap[coord[0]][1] - (player1.get_height()//2) 
        x2 = coordMap[coord[1]][0] - (player2.get_width()//2) 
        y2 = coordMap[coord[1]][1] - (player2.get_height()//2) 
        x3 = coordMap[coord[2]][0] - (player3.get_width()//2) 
        y3 = coordMap[coord[2]][1] - (player3.get_height()//2) 
    elif players == 4 and victory == False:
        x1 = coordMap[coord[0]][0] - (player1.get_width()//2) 
        y1 = coordMap[coord[0]][1] - (player1.get_height()//2) 
        x2 = coordMap[coord[1]][0] - (player2.get_width()//2) 
        y2 = coordMap[coord[1]][1] - (player2.get_height()//2) 
        x3 = coordMap[coord[2]][0] - (player3.get_width()//2) 
        y3 = coordMap[coord[2]][1] - (player3.get_height()//2) 
        x4 = coordMap[coord[3]][0] - (player4.get_width()//2) 
        y4 = coordMap[coord[3]][1] - (player4.get_height()//2) 

