def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass


'''General Gist:
    It's literally like tic-tac-toe, but I need to automate it.
    I'm given a list that looks like this:
        board7 = [
        ['X','X','O',''],
        ['O','X','O','O'],
        ['X','','','O'],
        ['O','X','','']
        ]
    from there, I need to know who the winner is
    
    
    HOW MIGHT WE:
        1) To identify who wins, I first need to know the ENTRIES in the board itself
            
        2) I know the entries, I evaluate them. 
            This is looking like three if elif else blocks
        3) Then, I return a specific winner
            I might not even need to explicitly write "X" or "O," cause I can just  
    
    SOME TACTICS I CAN USE:
        LIST CRAFTING
            Create a compilation/list of values in specific positions that might make a tic-tac-toe win
            check if all elements in that list are the same
            If they are, then we have a winner!
            If not, move on to the next list
        POSITIONS
            Turn the board into an entire list
            Create a formula that will get the nth position of the list (something like index + board num)
            check if they're all the same
            win
            lose'''

board6 = [
['O','X','O'],
['O','X','O'],
['','',''],
]

row = 0
column = 0
columnx = 0
diagonal = 0
x = 0
y = len(board6)-1
l = []
l2 =[]
l3 = []

#this is to check if there's a tic-tac-toe in the rows
while row != len(board6):
    if all(item == board6[row][0] for item in board6[row][0:len(board6)]):
        l.append(board6[row][0])
    row+=1


#this is to check if there's a tic-tac-toe in the columns
while column!= len(board6)-1:
    if all(item == board6[0][column] for item in board6[0:len(board6)-1][column][column]):
        l.append(board6[0][column])
    column+=1

#this is to check a tic-tac-toe in the diagonals
while diagonal != len(board6):
    l2.append(board6[diagonal][diagonal])
    diagonal+=1

#if there's a tic-tac-toe, the diagonal will be appended into the original list
if all(item == l2[0] for item in l2):
    l.append(l2[0])

#this is to check the OTHER diagonal
while x != len(board6):
    l3.append(board6[x][y])
    x += 1
    y -= 1

if all(item == l3[0] for item in l3):
    l.append(l3[0])

if l == [] or l == ['']:
    print("NO WINNER")

else:
    print(l[0])

print(l)


'''general idea for this:
    There are two moving variables that will allow me to check the columns
    The idea is it goes 0 1 2 for 0, 0 1 2 for 1, 0 1 2 for 2, etc...
    If 0 1 and 2 match for any 0, 1, or 2, then I can append it into l
        THIS PART IS HARD
    If not, I don't do anything.
    '''

''.join(board6[0:len(board6)-1])