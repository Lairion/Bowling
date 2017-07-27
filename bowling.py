class Player:
    def __init__(self,name):
        self.name = name
        self.points = []
def check_simple_throw(first_throw):
    if first_throw >= 10:
        points = [[first_throw,0,"X"]]
    else:
        second_throw = int(input("Second Throw: "))
        if first_throw+second_throw >= 10:
            points = [[first_throw,second_throw,"/"]]
        else:
            points = [[first_throw,second_throw,first_throw+second_throw]]
    return points
def check_special_throw(first_throw):
    if first_throw >= 10:
        second_throw = int(input("Second Throw: "))
        third_throw = int(input("Third Throw: "))
        points = [[first_throw,second_throw,third_throw,sum([first_throw,second_throw,third_throw])]]
        print(player.name,player.points)
    else:
        second_throw = int(input("Second Throw: "))  
        if second_throw+first_throw >= 10:               
            third_throw = int(input("Third Throw: "))
            points = [[first_throw,second_throw,third_throw,sum([first_throw,second_throw,third_throw])]]
        else:
            points = [[first_throw,second_throw,0,first_throw+second_throw]]
    return points

players = []
players_count = int(input("How many players? "))
for i in range(players_count):
    players.append(Player(input("Input name player "+str(i+1))))
for i in range(3):
    for player in players:
        print(player.name)
        first_throw = int(input("First Throw: "))
        if len(player.points)>1:
            if player.points[-2][2] == "X":
                player.points[-2][2] = 20 + first_throw
        if player.points:
            if player.points[-1][2]  == "X":
                if first_throw >= 10:
                    player.points+=[[first_throw,0,"X"]]
                    print(player.name,player.points)
                else:
                    second_throw = int(input("Second Throw: "))
                    player.points[-1][2]  = 10 + first_throw + second_throw
                    if second_throw+first_throw >= 10:
                        player.points+=[[first_throw,second_throw,"/"]]
                    else:
                        player.points+=[[first_throw,second_throw,first_throw+second_throw]]
                    print(player.name,player.points)
            elif player.points[-1][2]  == "/":
                player.points[-1][2] = 10 + first_throw 
                player.points += check_simple_throw(first_throw)
                print(player.name,player.points)
            else:
                player.points += check_simple_throw(first_throw)
                print(player.name,player.points)

        else:
            player.points += check_simple_throw(first_throw)
            print(player.name,player.points)


for player in players:
    first_throw = int(input("First Throw: "))
    if len(player.points)>1:
        if player.points[-2][2] == "X":
            player.points[-2][2] = 20 + first_throw
    if player.points[-1][2]  == "X":
        if first_throw >= 10:
            second_throw = int(input("Second Throw: "))
            player.points[-1][2]  = 10 + first_throw + second_throw
            third_throw = int(input("Third Throw: "))
            player.points+=[[first_throw,second_throw,third_throw,sum([first_throw,second_throw,third_throw])]]
            print(player.name,player.points)
        else:
            second_throw = int(input("Second Throw: "))  
            player.points[-1][2]  = 10 + first_throw + second_throw
            if second_throw+first_throw >= 10:               
                third_throw = int(input("Third Throw: "))
                player.points+=[[first_throw,second_throw,third_throw,sum([first_throw,second_throw,third_throw])]]
            else:
                player.points+=[[first_throw,second_throw,0,first_throw+second_throw]]
            print(player.name,player.points)
    elif player.points[-1][2]  == "/":
         player.points[-1][2] = 10 + first_throw
         player.points += check_special_throw(first_throw)
         
    else:
        player.points += check_special_throw(first_throw) 
        print(player.name,player.points)
for player in players:
    print(player.name,player.points)
    