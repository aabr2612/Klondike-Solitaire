def header():
    print("""
            #   # #      ###  #   # ####  ### #   # #####    #####   ###  #     ### #####   ###   ### ####   #####
            #  #  #     #   # ##  # #   #  #  #  #  #       ##      #   # #      #    #    ## ##   #  #   #  #    
            ###   #     #   # # # # #   #  #  ###   ####     #####  #   # #      #    #   #######  #  ####   #### 
            #  #  #     #   # #  ## #   #  #  #  #  #            ## #   # #      #    #   ##   ##  #  #   #  #    
            #   # #####  ###  #   # ####  ### #   # #####    #####   ###  ##### ###   #   ##   ## ### #    # #####
            """)
    
def main_menu():
    header()
    print("""
                                                    1. Play Game
                                                    2. Instructions
                                                    3. Exit
            """)
    option = input("                                                    Enter your choice: ")
    return option

def instructions_to_play_game():
    print("")
    
def game_menu():
    print("""
          1. Draw card from stock pile
          2. Move card
          3. Move multiple cards
          4. Exit""")
    option = input("          Enter your choice: ")
    return option