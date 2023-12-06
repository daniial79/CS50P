import sys
import csv
from tabulate import tabulate


def main():
    table = []
    filename = check_cmd_args()

    try:
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not found")
    else:
        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


def check_cmd_args() -> str:
    args = sys.argv

    if len(args) < 2:
        sys.exit("Too few command-line arguments")

    if len(args) > 2:
        sys.exit("Too many command-line arguments")

    if ".csv" not in args[1]:
        sys.exit("Not a CSV file")

    return args[1]


if __name__ == '__main__':
    main()
