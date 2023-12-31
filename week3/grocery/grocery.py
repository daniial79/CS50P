def main():
    grocery_list = {}

    while True:
        try:
            item = input().lower().strip()

            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            for key in sorted(grocery_list.keys()):
                print(grocery_list[key], key.upper())
            break


if __name__ == '__main__':
    main()
