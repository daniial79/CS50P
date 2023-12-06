months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        input_date = input("Enter your date in anno domini format: ").strip()

        if "/" in input_date:
            month, day, year = input_date.split("/")


            if not month.isnumeric():
                continue

            if (int(month) >= 1) and (int(month) <= 12) and (int(day) >= 1) and (int(day) <= 31):
                break
        elif "," in input_date:
            first_filter = input_date.split(",")
            year = first_filter[1]

            second_filter = first_filter[0].split(" ")

            if not second_filter[1].isnumeric():
                continue

            month_in_en = second_filter[0]
            day = second_filter[1]

            month = ""
            for i in range(len(months)):
                if months[i] == month_in_en:
                    month += f"{i+1}"

            if (int(month) >= 1) and (int(month) <= 12) and (int(day) >= 1) and (int(day) <= 31):
                break

    if int(day) < 10:
        day = "0" + day

    if int(month) < 10:
        month = "0" + month

    print(f"{year}-{month}-{day}")


if __name__ == '__main__':
    main()
