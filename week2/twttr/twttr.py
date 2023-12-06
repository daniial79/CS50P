def main():
    vowels = ["i", "o", "u", "e", "a"]
    result = ""

    text_input = input("Enter your text: ").strip()

    for char in text_input:
        if char.lower() in vowels:
            result += ""
        else:
            result += char

    print(result)


if __name__ == '__main__':
    main()
