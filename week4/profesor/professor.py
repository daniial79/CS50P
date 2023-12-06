from random import randint


def main():
    user_level = get_level()
    user_score = 0

    for _ in range(10):
        # generate operands
        op1, op2 = generate_integer(user_level)

        # give user three guesses
        error = 0
        while True:
            user_answer = int(input(f"{op1} + {op2} = "))

            if user_answer == op1 + op2:
                user_score += 1
                break
            else:
                print("EEE")
                error += 1

            # user failed to answer
            if error == 3:
                print(f"{op1} + {op2} = {op1 + op2}")
                break

    print(user_score)


def get_level() -> int:
    while True:
        try:
            level = int(input("Enter level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level: int) -> (int, int):
    operand1, operand2 = 0, 0
    if level == 1:
        operand1 = randint(0, 9)
        operand2 = randint(0, 9)
    elif level == 2:
        operand1 = randint(10, 99)
        operand2 = randint(10, 99)
    elif level == 3:
        operand1 = randint(100, 999)
        operand2 = randint(100, 999)

    return operand1, operand2


if __name__ == '__main__':
    main()
