menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}


def main():
    print("Welcome to Filipe's Taqueria :)")

    total_cost = 0
    while True:
        try:
            order = input("").strip().lower()
            if order in menu:
                total_cost += menu[order]
                print(f"Total: $", end="")
                print(f"{total_cost:.2f}")
        except EOFError:
            print()
            break


if __name__ == '__main__':
    main()
