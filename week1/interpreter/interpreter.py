def main():
    expression = input("Enter your arithmetic expression: ")
    try:
        result = eval(expression)
        print(f"{float(result):.1f}")
    except ZeroDivisionError:
        print("second operand in division can not be zero")


if __name__ == '__main__':
    main()
