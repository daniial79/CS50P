def main():
    text_input = input("Enter your text: ").strip()
    result = shorten(text_input)
    print(result)


def shorten(word: str) -> str:
    vowels = ["i", "o", "u", "e", "a"]
    result = ""

    for char in word:
        if char.lower() in vowels:
            result += ""
        else:
            result += char

    return result

if __name__ == '__main__':
    main()
