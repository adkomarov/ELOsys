class EloPlayer:
    def __init__(self, rating=1000, k=20):
        self.rating = rating
        self.k = k

    def expected_score(self, opponent):
        return 1 / (1 + 10**((opponent.rating - self.rating) / 400))

    def update_rating(self, opponent, score):
        expected = self.expected_score(opponent)
        self.rating += self.k * (score - expected)

class EloMatch:
    def __init__(self, player1, player2, p1_score, p2_score):
        self.player1 = player1
        self.player2 = player2
        self.p1_score = p1_score
        self.p2_score = p2_score

    def update_ratings(self):
        self.player1.update_rating(self.player2, self.p1_score)
        self.player2.update_rating(self.player1, self.p2_score)



player1 = EloPlayer()
player2 = EloPlayer()

match = EloMatch(player1, player2, 1, 0)
match1 = EloMatch(player1, player2, 0, 1)

match.update_ratings()
print("Player 1 rating:", player1.rating)
print("Player 2 rating:", player2.rating)
match1.update_ratings()

print("Player 1 rating:", player1.rating)
print("Player 2 rating:", player2.rating)

players = [EloPlayer(1000) for i in range(8)]

# Play matches between the players
matches = [(0, 4, 1, 0), (1, 5, 1, 0), (2, 6, 0.5, 0.5), (3, 7, 0, 1),
           (0, 5, 0.5, 0.5), (1, 4, 0, 1), (2, 7, 1, 0), (3, 6, 0, 1),
           (0, 6, 1, 0), (1, 7, 1, 0), (2, 4, 0.5, 0.5), (3, 5, 0, 1),
           (0, 7, 0, 1), (1, 6, 0.5, 0.5), (2, 5, 1, 0), (3, 4, 0.5, 0.5)]

for match in matches:
    player1, player2, p1_score, p2_score = match
    EloMatch(players[player1], players[player2], p1_score, p2_score).update_ratings()

rankings = sorted(players, key=lambda x: x.rating, reverse=True)

for i, player in enumerate(rankings):
    print("Rank {}: Player {} ({} rating)".format(i+1, players.index(player)+1, player.rating))
