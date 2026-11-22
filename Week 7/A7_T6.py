import random
random.seed(1234)

ROCK_ART = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
PAPER_ART = """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)"""
SCISSORS_ART = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
RPS_ARTS = [(0, 0),
            ("rock", ROCK_ART),
            ("paper", PAPER_ART),
            ("scissors", SCISSORS_ART)]
BEATS = {
    1: 3,
    2: 1,
    3: 2,
}


class RPC_result:
    def __init__(self):
        self.name = ""
        self.choice = 0
        self.wins = 0
        self.loses = 0
        self.draws = 0


def print_results(result_list: list[RPC_result]) -> None:
    print("\nResults:")
    for result in result_list:
        print("{name} - wins ({wins}), losses ({loses}), draws ({draws})".format(
            name=result.name, wins=result.wins, loses=result.loses, draws=result.draws))
    return None


def print_game(result_list: list[RPC_result]) -> None:
    print("Rock! Paper! Scissors! Shoot!\n")
    sep = "#" * 25
    for result in result_list:
        print(sep)
        print("{name} chose {rps}\n".format(
            name=result.name, rps=RPS_ARTS[result.choice][0]))
        print(RPS_ARTS[result.choice][1])
        print()
    print(sep)
    print()
    if BEATS[result_list[-1].choice] == result_list[-2].choice:
        print("{name1} {choice1} beats {name2} {choice2}".format(
            name1=result_list[-1].name,
            choice1=RPS_ARTS[result_list[-1].choice][0],
            name2=result_list[-2].name,
            choice2=RPS_ARTS[result_list[-2].choice][0]))
        result_list[-1].wins = result_list[-1].wins + 1
        result_list[-2].loses = result_list[-2].loses + 1
    elif BEATS[result_list[-2].choice] == result_list[-1].choice:
        print("{name2} {choice2} beats {name1} {choice1}".format(
            name1=result_list[-1].name,
            choice1=RPS_ARTS[result_list[-1].choice][0],
            name2=result_list[-2].name,
            choice2=RPS_ARTS[result_list[-2].choice][0]))
        result_list[-1].loses = result_list[-1].loses + 1
        result_list[-2].wins = result_list[-2].wins + 1
    else:
        print("Draw! Both players chose {choice}.".format(
            choice=RPS_ARTS[result_list[-1].choice][0]))
        result_list[-1].draws = result_list[-1].draws + 1
        result_list[-2].draws = result_list[-2].draws + 1
    return None


def main():
    print("""Program starting.
Welcome to the rock-paper-scissors game!""")
    result_list = [RPC_result() for _ in range(2)]
    result_list[0].name = input("Insert player name: ")
    print("Welcome {name}!".format(name=result_list[0].name))
    result_list[1].name = "RPS-3PO"
    print("""Your opponent is {bot_name}.
Game starts...""".format(bot_name=result_list[1].name))
    player_choice = 1
    while True:
        print("""\nOptions:
1 - Rock
2 - Paper
3 - Scissors
0 - Quit game""")
        player_choice_str = input("Your choice: ")
        try:
            player_choice = int(player_choice_str)
            if player_choice <= 0 or player_choice >= 4:
                raise ValueError
        except ValueError:
            player_choice = 0
            break
        result_list[0].choice = player_choice
        result_list[1].choice = random.randint(1, 3)
        print_game(result_list=result_list)
    print_results(result_list=result_list)
    print("\nProgram ending.")
    return None


if __name__ == "__main__":
    main()
