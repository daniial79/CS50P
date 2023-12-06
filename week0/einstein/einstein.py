def main():
    mass = int(input("Enter mass in kg: "))
    result = mass * (3e8 ** 2)
    print(f"{result:.0f}")


if __name__ == '__main__':
    main()
