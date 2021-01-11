#init
tab = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
player = 1
#making board
def make() :    
    print(" %c | %c | %c " % (tab[7],tab[8],tab[9]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (tab[4],tab[5],tab[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (tab[1],tab[2],tab[3]))    
    print("   |   |   ")  
#check game state (win/ongoing/tie)
def gameState() :
    #horizontal wins
    if(tab[1]==tab[2] and tab[2]==tab[3] and tab[1]!=' ') : 
        return "win"
    elif(tab[4]==tab[5] and tab[5]==tab[6] and tab[4]!=' ') : 
        return "win"
    elif(tab[7]==tab[8] and tab[8]==tab[9] and tab[7]!=' ') : 
        return "win"
    #vertical wins
    elif(tab[1]==tab[4] and tab[4]==tab[7] and tab[1]!=' ') : 
        return "win"
    elif(tab[2]==tab[5] and tab[5]==tab[8] and tab[2]!=' ') : 
        return "win" 
    elif(tab[3]==tab[6] and tab[6]==tab[9] and tab[3]!=' ') : 
        return "win" 
    #diagonal win
    elif(tab[1]==tab[5] and tab[5]==tab[9] and tab[1]!=' ') : 
        return "win" 
    elif(tab[3]==tab[5] and tab[5]==tab[7] and tab[3]!=' ') : 
        return "win" 
    #tie
    elif(tab[1]!=' ' and tab[2]!=' ' and tab[3]!=' ' and tab[4]!=' ' and tab[5]!=' ' and tab[6]!=' ' and tab[7]!=' ' and tab[8]!=' ' and tab[9]!=' ') : 
        return "tie"
    #game is still ongoing
    else :
        return "ongoing"
#init mark (x or o)
mark=""
#turn function
def play () :
    choice = 0
    #which player's turn
    if(player %2 == 0) :
        print("it's player 2's turn\n")
        mark= 'O'

    else : 
        print("it's player 1's turn\n") 
        mark='X'
    
    #making sure that the position exists
    while (choice <1 or choice > 9) :
        choice = int(input("choose where to put your mark (from 1 to 9) :")) 
    #making sure the case is empty
    while (tab[choice]!=' ') :
        print("case already occupied")
        #making sure that the position exists
        while (choice <1 or choice > 9) :
            choice = int(input("choose where to put your mark (from 1 to 9) :")) 
    tab[choice]=mark
    make()

playAgain="yes"
#a loop to play again after the end of a game
while(playAgain=="yes") :
    #initializing the board
    tab = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
    player= 1
    make()
    #playing when there's an empty case
    while(gameState()=="ongoing") : 
        play()
        player+=1
    #game result
    if(gameState()=="win") :
        if(player %2==0) :
            print("player 1 won") 
        else :
            print("player 2 won")
    else :
        print("it's a tie")
    playAgain = input("do you want to play again?(yes/no)")


