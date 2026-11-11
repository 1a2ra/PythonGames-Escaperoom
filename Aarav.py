def reactor_puzzle():
    print(
        "\033[91m"
        "==================================================\n"
        "WARNING: REACTOR CORE UNSTABLE\n"
        "=================================================="
        "\033[0m\n"

        "\033[93m"
        "Chief Engineer's Log"
        "\033[0m\n\n"

        "The thermal and electric subsystems are interacting\n"
        "in unexpected ways.\n\n"

        "Stabilise all 25 nodes within 35 moves or the station\n"
        "will be lost.\n\n"

        "\033[96m"
        "REACTOR STABILISATION PROTOCOL"
        "\033[0m\n\n"

        "Enter coordinates A1-E5\n"
        "Type HINT for engineering assistance\n"
        "Type QUIT to abort mission\n\n"

        "\033[92m"
        "T = Thermal Node\n"
        "E = Electric Node"
        "\033[0m\n\n"

        "\033[95m"
        "Thermal overload:"
        "\033[0m "
        "Vertically and horizontally neighbouring cells\n\n"

        "\033[94m"
        "Electric overload:"
        "\033[0m "
        "Diagonally neighbouring cells\n"
    )

    reactor = [
        [{"energy":4,"type":"T"},{"energy":7,"type":"E"},{"energy":3,"type":"T"},{"energy":5,"type":"E"},{"energy":4,"type":"T"}],
        [{"energy":6,"type":"E"},{"energy":5,"type":"T"},{"energy":8,"type":"E"},{"energy":2,"type":"T"},{"energy":1,"type":"E"}],
        [{"energy":2,"type":"T"},{"energy":4,"type":"E"},{"energy":7,"type":"T"},{"energy":3,"type":"E"},{"energy":5,"type":"T"}],
        [{"energy":8,"type":"E"},{"energy":1,"type":"T"},{"energy":6,"type":"E"},{"energy":4,"type":"T"},{"energy":7,"type":"E"}],
        [{"energy":3,"type":"T"},{"energy":5,"type":"E"},{"energy":2,"type":"T"},{"energy":8,"type":"E"},{"energy":4,"type":"T"}]
    ]

    row_letters = ["A", "B", "C", "D", "E"]
    cipher = "Alphabet"
    count = 0

    def print_grid():
        print("\n     1   2   3   4   5")
        for row in range(5):
            print(row_letters[row], end="   ")
            for col in range(5):
                node = reactor[row][col]
                print(f"{node['type']}{node['energy']}", end="  ")
            print()

    def thermal_overload(row, col):
        reactor[row][col]["energy"] = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 5 and 0 <= new_col < 5:
                reactor[new_row][new_col]["energy"] += 1

        print(
            f"\033[91mTHERMAL OVERLOAD "
            f"at {row_letters[row]}{col+1}\033[0m"
        )

    def electric_overload(row, col):
        reactor[row][col]["energy"] = 0

        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 5 and 0 <= new_col < 5:
                reactor[new_row][new_col]["energy"] += 1

        print(
            f"\033[94mELECTRIC OVERLOAD "
            f"at {row_letters[row]}{col+1}\033[0m"
        )

    def reactor_stable():
        for row in reactor:
            for node in row:
                if node["energy"] < 1 or node["energy"] > 5:
                    return False

        return True

    def find_overload():
        overload = []

        for row in range(5):
            for col in range(5):
                if reactor[row][col]["energy"] >= 10:
                    overload.append((row, col))

        return overload

    def resolve_reactor():
        overload = find_overload()
        safety_breakout = 0

        while overload and safety_breakout < 100:
            row, col = overload.pop(0)
            node_type = reactor[row][col]["type"]

            if node_type == "T":
                thermal_overload(row, col)
            else:
                electric_overload(row, col)

            overload = find_overload()
            safety_breakout += 1

    def hint_system():
        stable_nodes = 0

        for row in reactor:
            for node in row:
                if 1 <= node["energy"] <= 5:
                    stable_nodes += 1

        unstable_count = 25 - stable_nodes

        if unstable_count == 0:
            print("\nEngineering Note:")
            print("All reactor systems stable.")
            return

        if unstable_count > 15:
            print(
                "\nEngineering Note:\n"
                "Many systems remain unstable.\n"
                "Focus on reducing extremely high\n"
                "or extremely low energy values first."
            )
            return

        if unstable_count > 5:
            print(
                "\nEngineering Note:\n"
                "Remember:\n"
                "Thermal nodes affect vertical and horizontal neighbours.\n"
                "Electric nodes affect diagonal neighbours."
            )
            return

        for row in range(5):
            for col in range(5):
                energy = reactor[row][col]["energy"]

                if energy < 1 or energy > 5:
                    print(
                        f"\nEngineering Note:\n"
                        f"Node {row_letters[row]}{col+1} "
                        f"remains unstable.\n"
                        f"Current Energy = {energy}"
                    )
                    return

    while True:
        print_grid()

        node_charge = (
            input("\nEnter node: ")
            .strip()
            .replace(" ", "")
            .upper()
        )

        if node_charge == "QUIT":
            print("\nMission Aborted.")
            break

        if node_charge == "HINT":
            hint_system()
            continue

        if len(node_charge) != 2:
            print("Invalid input. Use A1-E5.")
            continue

        letter = node_charge[0]
        number = node_charge[1]

        if (
            letter not in row_letters
            or not number.isdigit()
            or not (1 <= int(number) <= 5)
        ):
            print("Invalid input. Use A1-E5.")
            continue

        target_row = row_letters.index(letter)
        target_col = int(number) - 1

        reactor[target_row][target_col]["energy"] += 1

        print(f"\nNode {letter}{number} charged.")

        resolve_reactor()
        count += 1

        stable_nodes = 0

        for row in reactor:
            for node in row:
                if 1 <= node["energy"] <= 5:
                    stable_nodes += 1

        print(f"\nStable Nodes: {stable_nodes}/25")
        print(f"Moves Remaining: {35-count}")

        if stable_nodes <= 5:
            print("\033[91mWARNING: Reactor highly unstable.\033[0m")
        elif stable_nodes >= 24:
            print("Final stabilisation required.")
        elif stable_nodes >= 20:
            print("Reactor fluctuations decreasing.")

        if reactor_stable():
            print_grid()

            efficiency = ((count) / 35)

            print(f"""
\033[92m==================================================
REACTOR STABILISED
==================================================\033[0m

Efficiency Rating: {efficiency}""")
            print("""
Bonus Hint:

Use alphabet positions.

Example:
A = 1
B = 2
C = 3
...
Z = 26
""")



            print("Code Chest 2:A_J4")

            return True

        if count == 35:
            print_grid()

            print("""
\033[91m==================================================
MISSION FAILED
==================================================\033[0m

The reactor could not be stabilised
within the allowed move limit.
""")
            print("Chest 2 code: A_J4\n Penalty:No bonus hint for you!")

            return False
if __name__ == "__main__":
     reactor_puzzle()


