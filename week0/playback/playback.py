def main():
    user_input = input("Enter your text: ")
    slowed_text = user_input.replace(" ", "...")
    print(slowed_text)


if __name__ == '__main__':
    main()
