def main():
    time_input = input("enter meal time: ").strip()
    converted_to_float = convert(time_input)

    if 7.00 <= converted_to_float <= 8.00:
        print("breakfast time")
    elif 12.00 <= converted_to_float <= 13.00:
        print("launch time")
    elif 18.00 <= converted_to_float <= 19.00:
        print("dinner time")


def convert(time: str) -> float:
    temp = time.split(":")
    return float(temp[0]) + (float(temp[1]) / 60)


if __name__ == '__main__':
    main()
