import os
import codecs

HERE = os.path.abspath(os.path.dirname(__file__))

EMPERORS = ["Galba", "Otho", "Vitellius", "Vespasian"]


def decipher_text(state: dict) -> None:
    ciphered_filename = "{next}_{passphrase}.gkg".format(
        next=state["next_location"], passphrase=state["passphrase"])
    ciphered_filename = os.path.join(HERE, ciphered_filename)
    plain_filename = "{next}_{plaintext}.txt".format(
        next=state["next_location"], plaintext=state["plain_text"])
    plain_filename = os.path.join(HERE, plain_filename)
    with open(ciphered_filename, encoding="utf-8", mode="r") as input_file:
        state["appended"] = input_file.readline()
        ciphered_content = input_file.read()
        plain_content = codecs.decode((ciphered_content), "rot13")
        with open(plain_filename, encoding="utf-8", mode="w") as output_file:
            output_file.write(plain_content)
    return None


def read_progress(filename: str) -> dict:
    with open(filename, encoding="utf-8", mode="r") as input_file:
        lines = input_file.readlines()
        keys = lines[0].strip().split(";")
        values = lines[-1].strip().split(";")
        result = dict(zip(keys, values))
        result["prior"] = "".join(lines)
        return result


def write_progress(filename: str, content: dict) -> None:
    with open(filename, encoding="utf-8", mode="w") as output_file:
        output_file.write(content["prior"])
        output_file.write(content["appended"])
    return None


def name_prcs(name: str) -> str:
    if not name.endswith("s"):
        return "{name}'s".format(name=name)
    else:
        return "{name}'".format(name=name)


def game_ops(state: dict) -> None:
    print("Travelling to {name} palace...". format(
        name=name_prcs(EMPERORS[int(state["next_location"]) - 1])))
    print("...Arriving to the {name} palace.".  format(
        name=name_prcs(EMPERORS[int(state["next_location"]) - 1])))
    state["plain_text"] = codecs.decode(state["passphrase"], "rot13")
    print("""Passing the guard at the entrance.
"{passphrase}!"
Looking for the message in the palace...
Ah, there it is! Seems cryptic.""".format(passphrase=state["plain_text"].capitalize()))
    decipher_text(state)
    write_progress(filename=os.path.join(HERE, "player_progress.txt"),
                   content=state)
    print("[Game] Progress autosaved!")
    print("""Deciphering Emperor's message...
Looks like I've got now the plain version copy of the Emperor's message.
Time to leave...""")
    return None


def main():
    print("Travel starting.")
    current_state = read_progress(os.path.join(HERE, "player_progress.txt"))
    if int(current_state["current_location"]) == 0:
        print("Currently at home.")
        game_ops(current_state)
    elif int(current_state["current_location"]) < 4:
        print("Currently at {name} palace.".format(
            name=name_prcs(EMPERORS[int(current_state["current_location"]) - 1])))
        game_ops(current_state)
    else:
        print("Travelling home...")
        print("...Arriving home")
        current_state["plain_text"] = codecs.decode(current_state["passphrase"], "rot13")
        decipher_text(current_state)
        write_progress(filename=os.path.join(HERE, "player_progress.txt"),
                       content=current_state)
        print("[Game] Progress autosaved!")
        print("Time to leave...")
    return None


if __name__ == "__main__":
    main()
