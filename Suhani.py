def escape_room(wordle_win,
    reactor_win,
    maze_win):
    import os
    import sys
    flag = 0

    CLEAR = "cls" if os.name == "nt" else "clear"

    def open_chest_1():
        os.system(CLEAR)
        print("----------------79---------------------")
        print("|                                     47")
        print("|                                      |")
        print("|                                      |")
        print("|             # *                      |")
        print("98                                     |")
        print("|                                      |")
        print("|                                      |")
        print("|             #                        |")
        print("|                                     33")
        print("|                                      |")
        print("|                                      |")
        print("---54------------------------16--------")
        print("You are now near the first chest. You can open it by the code received after solving the puzzle.")
        ##Rules of game 1
        input("Press Enter to play the puzzle....")
        os.system(CLEAR)
        ###FIRST GAME PUZZLE
        code = input("Enter the code to open the chest: ").strip()
        while code != "B@D!":
            print("Incorrect code. Please try again.")
            code = input("Enter the code to open the chest: ").strip()
        print("""
    Chest 1 Opened

    Recovered Fragment:
    L15
    """)
        input("Press Enter to continue...")

    def open_chest_2():
        os.system(CLEAR)
        print("----------------79---------------------")
        print("|                                     47")
        print("|                                      |")
        print("|                                      |")
        print("|             #                        |")
        print("98                                     |")
        print("|                                      |")
        print("|                                      |")
        print("|             # *                      |")
        print("|                                     33")
        print("|                                      |")
        print("|                                      |")
        print("---54------------------------16--------")
        print("You are now near the second chest. You can open it by the code received after solving the puzzle.")
        ##Rules of game 2
        input("Press Enter to play the puzzle....")
        os.system(CLEAR)
        ###Puzzle for second chest
        code = input("Enter the code to open the chest: ").strip()
        while code != "A_J4":
            print("Incorrect code. Please try again.")
            code = input("Enter the code to open the chest: ").strip()
        print("""
    Chest 2 Opened

    Recovered Fragment:
    ICA
    """)
        input("Press Enter to continue...")

    os.system(CLEAR)
    print("WELCOME TO THE ESCAPE-ROOM GAME")
    print("You are trapped in a room and you have to escape it by solving puzzles to open each chest.Each chest contain a clue for the escape.")
    print("You are inside one room with two chests and several doors. You can only enter one and only one door leads you to freedom")
    print("To find which door to go to, open each chest to find some clues.")
    print("* represents the player. - represents walls. number represents door number # represents chests")
    input("Press Enter to start the game...")
    os.system(CLEAR)
    print("----------------79---------------------")
    print("|                                     47")
    print("|                                      |")
    print("|                                      |")
    print("|             #                        |")
    print("98                                     |")
    print("|                                   *  |")
    print("|                                      |")
    print("|             #                        |")
    print("|                                     33")
    print("|                                      |")
    print("|                                      |")
    print("---54------------------------16--------")
    print("Enter your command to move the player.")
    print("The available commands are: go near chest 1, go near chest 2")
    command = input()
    command = command.lower().strip()

    while command != "go near chest 1" and command != "go near chest 2":
        os.system(CLEAR)
        print("----------------79---------------------")
        print("|                                     47")
        print("|                                      |")
        print("|                                      |")
        print("|             #                        |")
        print("98                                     |")
        print("|                                   *  |")
        print("|                                      |")
        print("|             #                        |")
        print("|                                     33")
        print("|                                      |")
        print("|                                      |")
        print("---54------------------------16--------")
        print("Invalid command. Please enter a valid command.")
        command = input("Enter your command: ")
        command = command.lower().strip()
    if command == "go near chest 1":
        open_chest_1()
        flag = 1
    elif command == "go near chest 2":
        open_chest_2()
        flag = 2
    print("Now open the other chest to find the other clues.")
    os.system(CLEAR)
    print("----------------79---------------------")
    print("|                                     47")
    print("|                                      |")
    print("|                                      |")
    print("|             #                        |")
    print("98                                     |")
    print("|                                   *  |")
    print("|                                      |")
    print("|             #                        |")
    print("|                                     33")
    print("|                                      |")
    print("|                                      |")
    print("---54------------------------16--------")
    command = input("Enter your command: ")
    command = command.lower().strip()
    while (command != "go near chest 1" or flag != 2) and (command != "go near chest 2" or flag != 1):
        os.system(CLEAR)
        print("----------------79---------------------")
        print("|                                     47")
        print("|                                      |")
        print("|                                      |")
        print("|             #                        |")
        print("98                                     |")
        print("|                                   *  |")
        print("|                                      |")
        print("|             #                        |")
        print("|                                     33")
        print("|                                      |")
        print("|                                      |")
        print("---54------------------------16--------")
        if (command == "go near chest 1" and flag == 1) or (command == "go near chest 2" and flag == 2):
            print("You have already opened this chest. Move closer to the other chest to open it.")
        else:
            print("Invalid command. Please enter a valid command.")
        command = input("Enter your command: ")
        command = command.lower().strip()
    if command == "go near chest 1" and flag == 2:
        open_chest_1()
    elif command == "go near chest 2" and flag == 1:
        open_chest_2()

    print("Congratulations! You have escaped one of the rooms. ")
    print("You enter another room and find one more chest. You can open this chest too by the code received after solving another puzzle.")
    print("----------------79---------------------------------------------------------")
    print("|                                       __   *                             |")
    print("|                                      |  |                                |")
    print("|                                      |  |                                |")
    print("|             #                        |  |                         #      |")
    print("98                                     |  |                                |")
    print("|                                      |  |                                |")
    print("|                                      |  |      ___________________       |")
    print("|             #                        |  ------[VICTORY DOOR:LOCKED]------")
    print("|                                     33")
    print("|                                      |")
    print("|                                      |")
    print("---54------------------------16--------")
    print("Enter your command to move the player.")
    print("The available commands are: go near chest 3")
    command = input()
    command = command.lower().strip()
    while command != "go near chest 3":
        os.system(CLEAR)
        print("----------------79---------------------------------------------------------")
        print("|                                       __   *                             |")
        print("|                                      |  |                                |")
        print("|                                      |  |                                |")
        print("|             #                        |  |                         #      |")
        print("98                                     |  |                                |")
        print("|                                      |  |                                |")
        print("|                                      |  |      ___________________       |")
        print("|             #                        |  ------[VICTORY DOOR:LOCKED]------")
        print("|                                     33")
        print("|                                      |")
        print("|                                      |")
        print("---54------------------------16--------")
        print("Invalid command. Please enter a valid command.")
        command = input("Enter your command: ")
        command = command.lower().strip()

    os.system(CLEAR)
    print("----------------79---------------------------------------------------------")
    print("|                                       __                                 |")
    print("|                                      |  |                                |")
    print("|                                      |  |                                |")
    print("|             #                        |  |                        * #     |")
    print("98                                     |  |                                |")
    print("|                                      |  |                                |")
    print("|                                      |  |      ___________________       |")
    print("|             #                        |  ------[VICTORY DOOR:LOCKED]------")
    print("|                                     33")
    print("|                                      |")
    print("|                                      |")
    print("---54------------------------16--------")
    print("You are now near the third chest. You can open it by the code received after solving the puzzle.")
    ##Rules of game 3
    input("Press Enter to play the puzzle....")
    os.system(CLEAR)
    ###Puzzle for third chest
    code = input("Enter the code to open the chest: ").strip()

    while code != "A0RU":
        print("Incorrect code. Please try again.")
        code = input("Enter the code to open the chest: ").strip()

    print("""
Chest 3 Opened

Recovered Fragment:
12

""")

    input("Press Enter to continue...")

    os.system(CLEAR)

    print("""
==================================================
              VICTORY DOOR
==================================================

==================================================
""")
    print("\nRecovered Information:\n")
    print("""Recovered
    Fragments:

    L15
    ICA
    12
    """)

    if wordle_win:
        print("- Numbers are not always numbers.")

    if reactor_win:
        print("- Use alphabet positions.")

    if maze_win:
        print("- A = 1, B = 2, ..., Z = 26")

    answer = input("Enter final keyword: ").strip().upper()

    while answer != "LOGICAL":
        print("\nACCESS DENIED.")
        print("Hint: convert the numbers into letters.")
        answer = input("Enter final keyword: ").strip().upper()

    os.system(CLEAR)

    print("""
==================================================
          VICTORY DOOR UNLOCKED
==================================================

Recovered String:

L15ICA12

Decoding:

15 -> O
12 -> L

Final Keyword:

LOGICAL

Congratulations!

You have reconstructed the final keyword,
opened the Victory Door,
and escaped the facility.

==================================================
""")