def process_input(min: int, max: int) -> int:
    choice_str = input("Your choice: ")
    try:
        choice = int(choice_str)
        if choice > max or choice < min:
            choice = -1
    except ValueError:
        choice = -1
    return choice