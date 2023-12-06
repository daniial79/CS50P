import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    if not re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        return False

    split_ip = ip.split(".")

    for part in split_ip:
        if int(part) > 255 or int(part) < 0:
            return False

    return True


if __name__ == '__main__':
    main()
