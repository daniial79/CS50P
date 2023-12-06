def main():
    plate_input = input("Enter your plate serial: ")
    print("Valid") if is_valid(plate_input) else print("Invalid")


def is_valid(plate: str) -> bool:
    if not 2 <= len(plate) <= 6:
        return False

    if not plate[0:2].isalpha():
        return False

    for index, char in enumerate(plate):
        if char.isnumeric():
            if char == "0":
                return False

            if plate[index:].isnumeric():
                break
            else:
                return False
    return True


if __name__ == '__main__':
    main()
