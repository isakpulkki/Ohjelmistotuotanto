class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.total = goals + assists
    
    def __str__(self):
        return self.name + ", from team " + self.team + " has scored " + str(self.goals) + " goals and " + str(self.assists) + "  assists, in total: " + str(self.total)
