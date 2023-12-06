def main():
    user_greeting = input("Enter the greeting word: ").strip().lower().split(" ")
    amount = 0
    if user_greeting[0][:5] == "hello":
        pass
    elif user_greeting[0][0] == "h":
        amount = 20
    else:
        amount = 100
    print(f"{amount}$")


if __name__ == '__main__':
    main()
