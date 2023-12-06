from math import floor


def main():
    number = get_proper_input()
    percentage = round_up_number(number)
    print_result(percentage)


def get_proper_input() -> float:
    while True:
        user_input = input("Enter fraction in X/Y format: ")
        try:
            splited_fraction = user_input.split("/")
            if float(splited_fraction[0]) > float(splited_fraction[1]) or ("." in splited_fraction[0]) or ("." in splited_fraction[1]):
                continue
            extracted_float = float(splited_fraction[0]) / float(splited_fraction[1])
        except ZeroDivisionError and ValueError:
            user_input = input("Enter fraction in X/Y format: ")
        else:
            return extracted_float


def round_up_number(f: float) -> float:
    return floor(round(f * 100, 0))


def print_result(f: float):
    if f <= 1:
        print("E")
    elif f >= 99:
        print("F")
    else:
        print(f"{f}%")


if __name__ == '__main__':
    main()
