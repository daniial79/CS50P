def main():
    result = "Adieu, adieu, to "
    names = []

    while True:
        try:
            user_input = input()
            names.append(user_input)
        except EOFError:
            break

    for index, name in enumerate(names):
        if len(names) == 1:
            result += name
            break

        if len(names) == 2:
            result += f"{names[0]} and {names[1]}"
            break

        if index == len(names) - 1:
            result += f"and {name}"
        else:
            result += f"{name}, "

    print(result)


if __name__ == '__main__':
    main()
