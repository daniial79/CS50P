def main():
    total_fetched = 0
    acceptable_coins = [5, 10, 25]

    while True:
        try:
            inserted_coin = int(input("Insert coin: "))

            if inserted_coin in acceptable_coins:
                total_fetched += inserted_coin

            if total_fetched >= 50:
                break

            print(f"Amount Due: {50 - total_fetched}")
        except ValueError:
            pass

    print(f"Change Owed: {total_fetched - 50}")


if __name__ == '__main__':
    main()
