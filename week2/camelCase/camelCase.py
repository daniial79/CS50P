def main():
    camel_case_input = input("Enter your name in camel case format: ")
    result = ""

    for char in camel_case_input:
        if 65 <= ord(char) <= 90:
            result += "_"
            result += char.lower()
        else:
            result += char

    print(result)


if __name__ == '__main__':
    main()
