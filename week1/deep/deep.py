def main():
    possible_answers = ["42", "forty two", "forty-two"]
    user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print("Yes") if user_answer.strip().lower() in possible_answers else print("No")


if __name__ == '__main__':
    main()
