print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
caminho1 = str(input('Você se encontra numa bifurcação , por onde seguir? ("E" ou "D") ')).lower()
if caminho1 == 'e':
    caminho2 = str(input('Você chegou a um lago , a uma ilha no meio , o que fazer (esperar um barco("E") ou nadar("N")) ')).lower()
    if caminho2 == 'e':
        caminho3 = str(input('Você conseguiu chegar na ilha ileso , nela a uma casa com 3 portas uma vermelha ("V"), uma amarela ("A"), e outra azul ("Az") , qual você escolhe ?' )).lower()
        if caminho3 == 'v':
            print('É um quarto cheio de fogo\nGAME OVER...')
        elif caminho3 == 'a':
            print('Você encontrou o tesouro!\nVOCÊ VENCEU')
        elif caminho3 == 'az':
            print('Você entrou em um quarto cheio de feras\nGAME OVER...')
        else:
            print('Você entrou em uma sala que não existe\nGAME OVER...')
    else:
        print('A correnteza é muito forte , você se afogou\nGAME OVER...')
else:
    print('Você caiu em um buraco\nGAME OVER...')





