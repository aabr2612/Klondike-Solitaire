import os
from game.game import Game

game = Game()
game.display()


while(True):
    os.system('cls')
    game.display()

    choice = input()

    if choice=="1":
        game.draw_card_from_stockpile()
    elif choice=="2":
        print(str(game.move_card_from_waste()))
        input("press key to continue!")