import sys
from task5definitions import *

def rouletteMode1 (numberOfGames, numberOfPlayers, playersNames, playersBets):
    gamesResults = []
    print("\nResults: \nGame    Win number")
    for i in range(numberOfGames):
        gamesResults.append(random.randint(0, 36))
        print("{}       {}".format(i + 1, gamesResults[i]))
    print("\nTotal number of players: {}\nTotal number of games: {}\n".format(numberOfPlayers, numberOfGames))
    for i in range(numberOfPlayers):
        numbersWon = []
        numbersLost = []
        for number in playersBets[playersNames[i]]:
            if int(number) in gamesResults:
                numbersWon.append(number)
            else:
                numbersLost.append(number)
        numbersWon = ', '.join(numbersWon)
        numbersLost = ', '.join(numbersLost)
        print("{}   Win: {}    Lost: {}".format(playersNames[i], numbersWon, numbersLost))

def rouletteMode2 (numberOfGames, numberOfPlayers, playersNames, playersBets):
    players = []
    games = []
    for i in range(numberOfPlayers):
        players.append(Player(playersNames[i], playersBets[playersNames[i]]))
    for i in range(numberOfGames):
        games.append(Game(i + 1))
        games[i].playAGame(players)
    print("\nSummary:")
    for game in games:
        game.printSummary()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        numberOfPlayers = int(sys.argv[1])
        numberOfGames = int(sys.argv[2])
        gameMode = int(sys.argv[3])
    else:
        sys.exit("Please enter three arguments")

    playersNames = []
    playersBets = {}
    for i in range(numberOfPlayers):
        playersNames.append(str(input("Name of player {} ".format(i + 1))))
        playersBets[playersNames[i]] = input("Enter your bets, separated by space ").split()
    if gameMode == 1:
        rouletteMode1(numberOfGames, numberOfPlayers, playersNames, playersBets)
    else:
        rouletteMode2(numberOfGames, numberOfPlayers, playersNames, playersBets)
