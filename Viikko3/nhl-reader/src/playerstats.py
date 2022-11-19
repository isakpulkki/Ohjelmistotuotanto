class PlayerStats:
    def top_scorers_by_nationality(self, players):
        print("Finnish players: ")
        sorted_players = sorted(players, key=lambda x: x.total, reverse=True)
        for player in sorted_players:
            print(player)