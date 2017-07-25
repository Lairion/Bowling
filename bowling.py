class Player:
    def __init__(self,name):
        self.name = name
        self.points = []
players = []
players_count = int(input("How many players?"))
for i in range(players_count):
    players.append(Player(input("Input name player "+str(i+1))))
for i in range(3):
    for player in players:
        first_throw = int(input("First Throw: "))
        if first_throw == 10:
            player.points+=[[first_throw,0,"X"]]
        else:
            second_throw = int(input("Second Throw: "))
            if first_throw+second_throw >= 10:
                player.points+=[[first_throw,second_throw,"/"]]
            else:
               player.points+=[[first_throw,second_throw,first_throw+second_throw]]
        print(player.name,player.points)
for player in players:
    print(player.name,player.points)