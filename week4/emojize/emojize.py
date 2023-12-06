import requests
from sys import exit
from sys import argv


def main():
    try:
        if len(argv) < 2:
            exit("Missing command-line argument")
        bitcoin_amount = float(argv[1])
    except ValueError:
        exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response_body = response.json()
    except requests.RequestException:
        exit("Something went wrong during api call")

    # "bpi" -> "USD" -> "rate_float"
    rate_for_usd = response_body["bpi"]["USD"]["rate_float"]
    total_price = bitcoin_amount * rate_for_usd

    print(f"${total_price:,.4f}")


if __name__ == '__main__':
    main()
