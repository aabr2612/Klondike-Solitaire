import os
from game_files.game import Game
import ui.ui

def main():
      os.system("cls")
      while(True):
            os.system("cls")
            menu_choice = ui.ui.main_menu()
            if menu_choice == "1":
                  game = Game()
                  while(True):
                        os.system("cls")
                        ui.ui.header()
                        game.display()
                        game_choice = ui.ui.game_menu()
                        if game_choice=="1":
                              game.draw_card_from_stockpile()
                        elif game_choice=="2":
                              source = input("          Enter the source(Tableau [T], Waste[W], Foundation[F]): ")
                              destination = input("          Enter the destination(Tableau [T], Foundation[F]): ")
                              source_index = 8
                              if source.capitalize()=="T" or source.capitalize()=="F":
                                    source_index = input("          Enter the source index: ")
                              destination_index = input("          Enter the destination index: ")
                              input("          "+game.move_card(source,destination,source_index,destination_index)+"Press any key to continue...")
                        elif game_choice=="3":
                              game.move_multiple_cards()
                        elif game_choice=="4":
                              break
                        else:
                              input("          Invalid choice! Press any key to continue...")

            elif menu_choice=="2":
                  os.system("cls")
                  ui.ui.instructions_to_play_game()
            elif menu_choice=="3":
                  input("                                                    Thanks for playing the game! Press any key to continue...")
                  break
            else:
                  input("                                                    Invalid choice! Press any key to continue...")
                        
if __name__ == "__main__":
    main()