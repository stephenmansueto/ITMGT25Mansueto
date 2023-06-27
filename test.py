def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    acc = 0
    #if there's no in-between the stops, just get the travel time between the two
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
                    print(int(route_map[key]['travel_time_mins']))
                    break
                else:
                    break
            index+=1
        for key in route_map:
            if second_stop in route_list[indexb][1]:
                acc+= int(route_map[key]['travel_time_mins'])
                print(int(route_map[key]['travel_time_mins']))
                break
            indexb+= 1
        if index<indexb:
            index+=1
            while index!=indexb:
                # print(index)
                acc+= int(route_map[route_list[index]]['travel_time_mins'])
                print(int(route_map[route_list[index]]['travel_time_mins']))
                index+=1
        elif indexb<index:
            index+=1
            while index!= len(route_map):
                acc+= int(route_map[route_list[index]]['travel_time_mins'])
                print(int(route_map[route_list[index]]['travel_time_mins']))
                index+=1
            indexb = 0
            while second_stop not in route_list[indexb][1]:
                acc+= int(route_map[route_list[indexb]]['travel_time_mins'])
                indexb+=1
                


    return acc













x = eta('a3', 'b3', {
        ('a1', 'a2'): {
            'travel_time_mins': 1
        },
        ('a2', 'a3'): {
            'travel_time_mins': 2
        },
        ('a3', 'b1'): {
            'travel_time_mins': 3
        },
        ('b1', 'b2'): {
            'travel_time_mins': 4
        },
        ('b2', 'b3'): {
            'travel_time_mins': 5
        },
        ('b3', 'c1'): {
            'travel_time_mins': 6
        }, 
        ('c1', 'c2'): {
            'travel_time_mins': 7
        },
        ('c2', 'c3'): {
            'travel_time_mins': 8
        },
        ('c3', 'a1'): {
            'travel_time_mins': 9
        }
    })

print(x)