def main():
    number = input("Fraction: ")
    percentage = convert(number)
    result = gauge(percentage)
    print(result)


def convert(fraction: str) -> int:
    while True:
        index = fraction.find("/")
        try:
            numerator = int(fraction[:index])
            denominator = int(fraction[index + 1:])

            ratio = numerator / denominator
            if ratio <= 1:
                return int(ratio * 100)
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage: int) -> str:
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == '__main__':
    main()
