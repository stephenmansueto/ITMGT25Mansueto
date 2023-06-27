'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        r_stat = "friends"

    elif to_member in social_graph[from_member]["following"]:
        r_stat = "follower"

    elif from_member in social_graph[to_member]["following"]:
        r_stat = "followed by"

    else:
        r_stat = "no relationship"

    return r_stat 


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    row = 0
    column = 0
    diagonal = 0
    x = 0
    y = len(board)-1
    l = []
    l2 =[]
    l3 = []
    vertical_board = list(zip(*board))

    #this is to check if there's a tic-tac-toe in the rows
    while row != len(board):
        if all(item == board[row][0] and item != '' for item in board[row][0:len(board)]):
            l.append(board[row][0])
        row+=1

    #this is to check if there's a tic-tac-toe in the columns
    while column != len(board):
        if all(item == vertical_board[column][0] and item != '' for item in vertical_board[column][0:len(board)]):
            l.append(vertical_board[column][0])
        column+=1

    #this is to check a tic-tac-toe in the diagonals
    while diagonal != len(board):
        l2.append(board[diagonal][diagonal])
        diagonal+=1

    #if there's a tic-tac-toe, the diagonal will be appended into the original list
    if all(item == l2[0] for item in l2):
        l.append(l2[0])

    #this is to check the OTHER diagonal
    while x != len(board):
        l3.append(board[x][y])
        x += 1
        y -= 1

    if all(item == l3[0] for item in l3):
        l.append(l3[0])

    if ('' in l and "X" not in l and "O" not in l) or l == []:
        winner = "NO WINNER"

    else:
        winner = l[0]

    return winner


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    acc = 0
    if (first_stop, second_stop) in route_map:
        acc = int(route_map[first_stop, second_stop]['travel_time_mins'])
    #if the first stop is the same as the second stop, then there's no travel time
    elif first_stop == second_stop:
        acc+= 0
    #what if there are in-betweens?
    else:
        route_list = list(route_map.keys())
        index = 0
        indexb = 0
        #the code below basically accumulates the value of the first and second stop. The while loop accounts for in-betweens
        for key in route_map:
            if first_stop in route_list[index][0]:
                if index>indexb or index == indexb:
                    acc+= int(route_map[key]['travel_time_mins'])
                    break
                else:
                    break
            index+=1
        for key in route_map:
            if second_stop in route_list[indexb][1]:
                acc+= int(route_map[key]['travel_time_mins'])
                break
            indexb+= 1
        if index<indexb:
            index+=1
            while index!=indexb:
                acc+= int(route_map[route_list[index]]['travel_time_mins'])
                index+=1
        elif indexb<index:
            index+=1
            while index!= len(route_map):
                acc+= int(route_map[route_list[index]]['travel_time_mins'])
                index+=1
            indexb = 0
            while second_stop not in route_list[indexb][1]:
                acc+= int(route_map[route_list[indexb]]['travel_time_mins'])
                indexb+=1
    return acc