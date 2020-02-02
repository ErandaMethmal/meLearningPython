game = [[1, 0, 1], 
        [2, 2, 2], 
        [1, 0, 1]]


def game_board(game_map,player =0,row=0,column = 0,just_display = False):
    try:
        if not just_display:
            game[row][column] = player
        print("   a  b  c")
        for index, row in enumerate(game):
            print(index, row)
        return game_map
    except IndexError as e:
        print("Somethings wrong",e)
    except Exception as e:
        print("Something went really bad")
        
      
def select_winner(game_map):
   
   #horizontal winners
    for row in game_map:
        if row.count(row[0])==len(row) and row[0] != 0:
            print("winner")
    
    #verticle winners
    for colIndex in range(len(game_map)):
        check = []
        for row in game_map:
            check.append(row[colIndex])
            
        if check.count(check[0])==len(check) and check[0] != 0:
                print("winner")
    
    #diagnol winners
    diags = [];
    for ix in range(len(game_map)):
        diags.append(game_map[ix][ix])
    if diags.count(diags[0])==len(diags):
            print("Winner top")
    diags = []; 
    for col,row in zip(reversed(range(len(game_map))),range(len(game))):  
        diags.append(game_map[row][col])
    if diags.count(diags[0])==len(diags):
        print("Winner bot")
    
  
    
game = game_board(game,1,1,1,False )

select_winner(game)