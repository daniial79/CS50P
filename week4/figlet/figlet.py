from sys import argv
from sys import exit
from pyfiglet import Figlet
from pyfiglet import FigletFont


def main():
    # checking the command line arguments
    if len(argv) not in [1, 3]:
        exit("Invalid usage")

    if argv[1] not in ["-f", "--font"]:
        exit("Invalid usage")

    if argv[2] not in FigletFont.getFonts():
        exit("Invalid usage")

    # get the text
    text = input("Enter your text: ")

    # render the text in proper font
    f = Figlet(font=argv[2])
    print(f.renderText(text))


if __name__ == '__main__':
    main()
