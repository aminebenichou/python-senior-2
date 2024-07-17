cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def drawTable():
    print(f"  {cells[0]} |  {cells[1]} |  {cells[2]} ")
    print("____|____|____")
    print(f"  {cells[3]} |  {cells[4]} |  {cells[5]} ")
    print("____|____|____")
    print(f"  {cells[6]} |  {cells[7]} |  {cells[8]} ")
    print("    |    |    ")
    
drawTable()
player = 'x'
turn = 0

# get win
def checkWin(player):
    y = 0
    while y<9:
        if cells[y] == cells[y+1] == cells[y+2] == player:
            return True
        y+=3
    y = 0
    while y<3:
        if cells[y] == cells[y+3] == cells[y+6] == player:
            return True
        y+=1
    
    if cells[0] == cells[4] == cells[8] == player:
        return True
    
    if cells[2] == cells[4] == cells[6] == player:
        return True
    return False

while True:
    if checkWin(player) :
        print(f"{player} has won")
        break
    i=0
    placement = input("Enter a number between 1 and 9: ")
    if placement not in cells :
        print("invalid position")
    if turn%2 != 0 :
        player = "o"
    else :
        player = "x"
    while i<len(cells):
        if cells[i] == placement:
            cells[i] = player
            drawTable()
        i += 1
    turn += 1
