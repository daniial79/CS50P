from random import randint

def main():
    while True:
        try:
            level = int(input("Enter level: "))
            if level > 0:
                break
        except ValueError:
            pass

    random_number = randint(1, level)

    while True:
        try:
            user_guess = int(input("guess the number: "))

            if user_guess < 0:
                print("only positive integers")
                continue

            if user_guess == random_number:
                print("Just right!")
                break
            elif user_guess < random_number:
                print("Too small!")
            elif user_guess > random_number:
                print("Too large!")
        except ValueError:
            print("only positive integers")


if __name__ == '__main__':
    main()
    