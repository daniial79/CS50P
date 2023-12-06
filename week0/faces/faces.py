def main():
    user_input = input("Enter your text: ")
    modified_text = convert(user_input)
    print(modified_text)


def convert(text: str) -> str:
    return text.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == '__main__':
    main()
