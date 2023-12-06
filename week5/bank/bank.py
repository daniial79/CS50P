def main():
    user_greeting = input("Enter the greeting word: ").strip().lower()
    amount = value(user_greeting)

    print(f"{amount}$")


def value(text: str) -> int:
    listed_text = text.split(" ")
    amount = 0
    if listed_text[0][:5] == "hello":
        pass
    elif listed_text[0][0] == "h":
        amount = 20
    else:
        amount = 100

    return amount


if __name__ == '__main__':
    main()
