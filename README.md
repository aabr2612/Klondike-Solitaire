# CS200M24PID73

# Solitaire Classic

<!-- Introduction -->
## Introduction
    Klondike Solitaire is a classic game implemented in python using different custom built data structures i.e., Stack, Queue and Linkedlist. It consists of 52 cards the user has to move all these cards to their foundations by making moves from tableaus and stock piles to ensure a win.

<!-- Key Features -->
## Features
    Here are some of the important features implemented in the game:

### 1. Single card movements:
        Single cards can be moved between foundation, tableaus and waste pile.
### 2. Multiple card movements:
        Multiple cards can be moved at a time from tableau to tableau on the basis of their ranks and suits validations.

### 3. Draw card from stockpile:
        Card can be drawn from the stock pile to waste pile so that the top card in waste pile is visible and able to be moved.

### 4. Move validations:
        Game validations logic has been implemented to ensure that the single or multiple card movement is valid by checking their ranks, suits and source and destination points to ensure game flow.

### 5. Instructions:
        Help and Rules menu has been made so that user can read and play the game and perform actions according to game rules.

### 6. Win Game:
        If user places all the cards into the foundations, it wins the game which then shows the number of moves and congratulations message.

<!-- Backend Files -->
## Backend:
    For backend we have following:

### 1. Card.py:
        Card class implementation with attributes suit, rank, face_down and name.

### 2. Deck.py:
        Deck class array of 52 cards. It loads, shuffles and then allows to draw these by using method 'draw_card' which is used in game to distribute cards among tableau and foundation.

### 3. LinkedList.py:
        Linkedlist datastructure is implemented in it used to make stacks used for tableaus and foundations. It helps in moving multiple cards in between the tableaus and other piles.

### 4. Queue.py:
        Queue datastructure is implemented using two stacks to implement the stock pile and waste pile functionality in the game. It allows us to draw card from stock to waste and draw top card from the waste pile.

### 5  Stack.py:
        Stack datastructure is implemented using linkedlist which helps in implementing the tableaus and the foundation piles along with the queue class which is used as stockpile.

### 6. Game.py:
        Game class implemented which initializes the tableaus, foundations, stockpile and deck. Then it used deck to distribute the cards among the tableaus and stockpile. It contains all the logics for the card movements and multiple card movements.

### 7. Utility.py:
        Utility file contains the validation functions to ensure the indexes and piles to ensure that card is moved in correct destination from source.

<!-- Frontend Files -->
## Frontend:
    For frontend we have following:

### UI.py:
        UI contains the header and other menus implementation along with win game menu which is implemented in CLI which allows the user to interact with the backend to perform tasks using the ui.

### Main.py:
        Main file contains all the driver code which interacts with the UI and Game files to make a flow of the game.

<!-- Game flow and structure-->
### Game flow:
    The game flow continues as:
        On running the main.py file a main menu appears with header and options:
        -- 1. Play Game
            If the user wants to play the game, further the game is printed and a sub menu of game appears:
                -- 1. Draw card
                    Allowing user to draw card from stockpile
                -- 2. Move card
                    Allowing user to move single card from between the game piles.
                -- 3. Move multiple cards:
                    Allowing the user to move multiple cards from one pile to other in the game.
                -- 4. Exit:
                    Ends the current game
        -- 2. Instructions
            Displays all the instructions to play the game.
        -- 3. Exit
            Closes the game

    Here is the folder structure for the game:

        CS200M24PID73
        ├── Classes
        │   ├── card.py   
        │   ├── deck.py  
        │   ├── linkedlist.py
        │   ├── queue.py
        │   └── stack.py
        ├── Game Files
        │   ├── game.py
        │   └── utility.py
        ├── UI
        │   └── ui.py
        └── main.py


<!-- How to run game -->
### How run game:
    To run this game simply clone the repository:
        `git clone https://gitlab.com/aabr2612/cs200m24pid73`
    
    Then run the `main.py` file to run the game.