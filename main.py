from Tesst import play
from Aarav import reactor_puzzle
from Ayana import maze_game
from Suhani import escape_room

print("===================================")
print("      THE PUZZLE ADVENTURE")
print("===================================")

wordle_win = play()

reactor_win = reactor_puzzle()

maze_win = maze_game()

escape_room(
    wordle_win,
    reactor_win,
    maze_win
)