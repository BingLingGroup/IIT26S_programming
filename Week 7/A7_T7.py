import os
from string import ascii_uppercase as UPPER_CASES

HERE = os.path.abspath(os.path.dirname(__file__))


def read_config(filename: str) -> list[str]:
    rotors = []
    filename = os.path.join(HERE, filename)
    with open(filename, encoding="utf-8", mode="r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            content = line.strip().split(":")
            rotors.append(content[1])
    return rotors


# wrong versions. without the output offset
# def char_to_left(char: str, rotor: str, offset: int) -> str:
#     index = UPPER_CASES.index(char.upper())
#     index = (index + offset) % len(UPPER_CASES)
#     return rotor[index]
# def char_to_right(char: str, rotor: str, offset: int) -> str:
#     index = rotor.index(char.upper())
#     index = (index - offset) % len(UPPER_CASES)
#     return UPPER_CASES[index]


def offset_input(char, position):
    index = UPPER_CASES.index(char)
    return (index + position) % len(UPPER_CASES)


def offset_output(index, position):
    return (index - position) % len(UPPER_CASES)


# reversed versions (javascript versions)
def char_to_left(char, rotor, position):
    output_c = UPPER_CASES[offset_input(char=char,
                                        position=position)]
    output_index = rotor.index(output_c)
    return UPPER_CASES[offset_output(index=output_index,
                                     position=position)]


def char_to_right(char, rotor, position):
    output_c = rotor[offset_input(char=char,
                                  position=position)]
    output_index = UPPER_CASES.index(output_c)
    return UPPER_CASES[offset_output(index=output_index,
                                     position=position)]


# correct versions
# def char_to_left(char, rotor, position):
#     output_c = rotor[offset_input(char=char, position=position)]
#     output_index = UPPER_CASES.index(output_c)
#     return UPPER_CASES[offset_output(index=output_index, position=position)]
# def char_to_right(char, rotor, position):
#     output_c = UPPER_CASES[offset_input(char=char, position=position)]
#     output_index = rotor.index(output_c)
#     return UPPER_CASES[offset_output(index=output_index, position=position)]


def calculate_offset(offsets: list[int]) -> None:
    offsets[0] = offsets[0] + 1
    i = 0
    while i < 2:
        if offsets[i] > 25:
            offsets[i] = 0
            offsets[i + 1] = offsets[i + 1] + 1
        i = i + 1
    if offsets[2] > 25:
        offsets[2] = 0
    return None


def enigma_encrypt(char: str, configs: list[str], positions: list[int]) -> str:
    result_char = char
    i = 0
    reflector = configs[-1]
    rotors = configs[:-1]
    calculate_offset(positions)
    for rotor in rotors:
        result_char = char_to_left(char=result_char,
                                   rotor=rotor,
                                   position=positions[i])
        i = i + 1
    result_char = char_to_left(char=result_char,
                               rotor=reflector,
                               position=0)
    i = i - 1
    for rotor in rotors[::-1]:
        result_char = char_to_right(char=result_char,
                                    rotor=rotor,
                                    position=positions[i])
        i = i - 1
    return result_char


def main():
    config_filename = input("Insert config(filename): ")
    configs = read_config(config_filename)
    positions = [0, 0, 0]
    input("Insert plugs (y/n)?: ")
    print("""No extra plugs inserted.
Enigma initialized.""")
    row = input("\nInsert row (empty stops): ")
    while row:
        converted_row = ""
        for char in row:
            char_out = enigma_encrypt(char=char.upper(),
                                      configs=configs,
                                      positions=positions)
            print("Character \"{char_in}\" illuminated as \"{char_out}\"".format(
                char_in=char,
                char_out=char_out))
            converted_row = converted_row + char_out
        print("Converted row - \"{converted}\".".format(
            converted=converted_row))
        positions = [0, 0, 0]
        row = input("\nInsert row (empty stops): ")
    print("\nEnigma closing.")
    return None


if __name__ == "__main__":
    main()
