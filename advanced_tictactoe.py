import itertools

def game_board(game_map,player =0,row=0,column = 0,just_display = False):
    try:
        if game_map[row][column] != 0:
            print("Not Allowed : Choose another location ")
            return game_map,False
        if not just_display:
            game[row][column] = player
        print("   "+"  ".join(str(i) for i in range(len(game_map))))
        for index, row in enumerate(game):
            print(index, row)
        return game_map,True
    except IndexError as e:
        print("Somethings wrong",e)
        return game_map,False
    except Exception as e:
        print("Something went really bad")
        return game_map,False
      
def select_winner(game_map):

    def all_same(check_list):
        if check_list.count(check_list[0])==len(check_list) and check_list[0] != 0:
            return True
        else:
            return False 
              
   #horizontal winners
    for row in game_map:
        if all_same(row):
            print("Winner  : Horizontally : ",row[0])
            return True
    
    #verticle winners
    for colIndex in range(len(game_map)):
        check = []
        for row in game_map:
            check.append(row[colIndex])
            
        if all_same(check):
            print("winner : Vertically : ",check[0])
            return True
    
    #diagnol winners
    diags = [];
    for ix in range(len(game_map)):
        diags.append(game_map[ix][ix])
    if all_same(diags):
            print("Winner : Diagonally : ",diags[0])
            return True
    diags = []; 
    for col,row in zip(reversed(range(len(game_map))),range(len(game))):  
        diags.append(game_map[row][col])
    if all_same(diags):
        print("Winner : Diagonally  : ",diags[0])
        return True
    return False
    
play_game=True
while play_game:
     game = [[0,0,0],
             [0,0,0],
             [0,0,0]]
     game_won = False
     player_choise = itertools.cycle([1,2])
     game,_ = game_board(game,just_display=True) #underscore igonores return value.
     while not game_won: 
        player_number = next(player_choise)
        played = False
        while not played:
            print(f"------------------ Player : {player_number}  -------------")
            row_choise = int(input("Please enter a row value to change (0,1,2) : "))
            column_choice = int(input("Please enter column value to change (0,1,2) : "))
            print("-----------------------------------------------")
            game,played = game_board(game,player_number,row_choise,column_choice,just_display=False)
        
        if select_winner(game):
            game_won = True
            play_again = input("Do you want to play again ? (y/n) : ")
            if play_again.lower()=='y':
                print("-----------------------------------------------")
                print("---------- Restarting the Game ----------------")
                print("-----------------------------------------------")
                print("-----------------------------------------------")
            elif play_again.lower()=='n':
                play_game = False
            else:
                print("-----------------------------------------------")
                print("-------Invalid input...Exiting now......-------")
                print("-----------------------------------------------")
                print("-----------------------------------------------")
                play_game = False
                
#TODO : Implement dynamic game size             
def dynamic_gamesize():
    game_size = 3
    game_map = [[0 for i in range(game_size)] for i in range(game_size)]
    print(game)