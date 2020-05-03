import random

class Player:
    def __init__ (self, playerName, playerBets):
        self.playerName = playerName
        self.playerBets = playerBets

    def setNewBets (self, bets):
        self.playerBets = bets

class Game:
    def __init__ (self, gameNumber):
        self.gameNumber = gameNumber
        self.bets = []
        self.winningNumber = 0
        self.winners = []

    def readNewBets (self, player):
        bets = input("{}, enter your bets, separated by spaces ".format(player.playerName)).split()
        player.setNewBets(bets)

    def roll (self):
        self.winningNumber = random.randint(0, 36)

    def checkWinningNumbers (self, player):
        if str(self.winningNumber) in player.playerBets:
            return True

    def playAGame (self, players):
        for player in players:
            if self.gameNumber != 1:
                self.readNewBets(player)
            self.bets.extend(x for x in player.playerBets if x not in self.bets)
        self.roll()
        for player in players:
            if self.checkWinningNumbers(player):
                self.winners.append(player.playerName)
        print("Winners: {}".format(', '.join(self.winners)))

    def printSummary (self):
        print("Game number: {}".format(self.gameNumber))
        print("Bet numbers: {}".format(', '.join(self.bets)))
        print("Winning number: {}".format(self.winningNumber))
        print("Winners: {}\n".format(', '.join(self.winners)))