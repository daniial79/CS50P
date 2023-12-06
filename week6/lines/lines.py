import sys


def main():
    filename = check_cmd_arg()

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        lines_count = 0
        for line in lines:
            if line_is_valid(line):
                lines_count += 1

    print(lines_count)


def check_cmd_arg() -> str:
    args = sys.argv

    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")

    if ".py" not in args[1]:
        sys.exit("Not a Python file")

    return args[1]


def line_is_valid(line: str) -> bool:
    if line.isspace():
        return False

    if line.lstrip().startswith("#"):
        return False

    return True


if __name__ == '__main__':
    main()
