from random import choice

continents = {
    "Asia": ["iran", "turkey", "russia", "pakistan", "afghanistan", "japan", "china", "thailand", "india"],
    "Europe": ["france", "germany", "italy", "netherland", "greece", "switzerland", "poland", "sweden"],
    "North America": ["america", "canada", "mexico", "jamaica", "cuba", "guatemala", "honduras"],
    "South America": ["brazil", "argentina", "peru", "venezuela", "chile", "colombia", "ecuador"],
    "Africa": ["nigeria", "morocco", "ghana", "tanzania", "senegal", "mali", "sudan"],
    "Australia": ["australia", "fiji"]
    
}

affirmative_sentences = [
    "Bingo, guessed right",
    "Well done matem keep going",
    "That's it, killing it.",
    "Baam. you are a natural.",
    "Bravo.",
    "quiet right."
]

negative_sentences = [
    "Missed that one champ.",
    "Hmph, guess again."
    "Not that easy isn't it?",
    "Push your brain ;).",
    "Maybe next time"
]

def get_user_prompt():
    print("Choose one of continets below to start the game:")
    
    for index, continent in enumerate(continents.keys()):
        print(f"{index + 1} => {continent}")
        
    user_input = input("enter number of continent: ")
    
    while user_input not in continents.keys():
    
        print("\n"+"#"*10)
        print("Invalid continent name.")    
        print("#"*10+"\n")
    
        user_input = input("enter continent name: ")

    return user_input


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]        
        
        
def character_is_valid(char: str) -> bool:
    return len(char) == 1 and 97 <= ord(char) <= 122
        
        
def update_name_container(container: list[str] , char: str, indecies: list[int]) -> list[str]:
    for i in indecies:
        container[i] = char
    return container
        
        
def is_session_finished(country: str, container: list[str]) -> str:
    return country == "".join(container)


def run_game_session(country_name: str) -> str:
    chances = len(country_name)
    container = ["-"] * chances
    
    print(f"\nyou have {chances} chances! good luck!")
    print("".join(container)+"")
    
    while chances > 0:
        user_guess = input("\nwrite your guess: ")

        # check for valid character
        if not character_is_valid(user_guess):
            print("\n"+"#" * 10)
            print("Invalid character.")
            print("#" * 10)
            continue
        
        indecies = find(country_name, user_guess)
        
        # check for repeated character
        if user_guess in container:
            print("\nyou already have gussed this character :/")
            print("".join(container))
            continue
        
        if len(indecies) != 0:
            # update the container
            container = update_name_container(container, user_guess, indecies)
            
            # check for end game
            if is_session_finished(country_name, container):
                return f"\nBingo. your word was {country_name}."
            
            # show the updated container
            print(f"\n{choice(affirmative_sentences)}")
            print("".join(container))
        else:
            # handling the wrong character guess
            print(f"\n{choice(negative_sentences)}. you have {chances-1} to go!")
            print("".join(container))
            chances -= 1
    return f"\nGame over. your word was {country_name}"

def main():
    print("Welcome to hangman game.")
    print("Choose a continent.\nyour word would be a country name.")
    print("press ctrl + C to exit the game.")
    print("#" * 60)
    
    while True:
            
        try:
            # get user prompt
            user_input = get_user_prompt()
            
            # choose a random country name based on user continet choice
            country = choice(continents[user_input])

            # create a game session
            result = run_game_session(country)
            print(result)
            print("#" * 10+"\n")
            
            # ask for another round
            if again := input("ready for another round?[y/n]: ") not in ["y", "Y"]:
                raise KeyboardInterrupt
                
            
        except (KeyboardInterrupt, EOFError):
            print("\ngood bye ;)")
            return


if __name__ == "__main__":
    main()