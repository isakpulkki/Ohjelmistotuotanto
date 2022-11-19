
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    players = reader.get_players()
    stats = PlayerStats()
    stats.top_scorers_by_nationality(players)

if __name__ == "__main__":
    main()
