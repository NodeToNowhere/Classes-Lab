class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach

    points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, name):
        return name in self.players

    def play_game(self, bool):
        if bool == True:
            self.points += 3
