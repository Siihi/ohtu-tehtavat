import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
        
class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.makeplayers()
        
    def makeplayers(self):
        players = []
    
        for player_dict in self.response:
            player = Player(
                player_dict["name"],
                player_dict["nationality"],
                player_dict["goals"],
                player_dict["assists"]
            )
        
            players.append(player)
        
        return players

class PlayerStats:
    def __init__(self, players):
        self.players = players
        
    def top_scorers_by_nationality(self, nationality):
        players = []
        players = filter(lambda player: player.nationality == nationality, self.players)
        players = sorted(players, key=lambda player: players.goals + players.assists, reverse = True)
        return players
    
if __name__ == "__main__":
    main()
