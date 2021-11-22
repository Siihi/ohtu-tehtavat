class Player:
    def __init__(self, name, nationality, goals, assists):
        self.name = name
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return f"{self.name:21} nationality {self.nationality:5} goals {str(self.goals):2} + {str(self.assists):2} = {str(self.goals+self.assists):2}"
