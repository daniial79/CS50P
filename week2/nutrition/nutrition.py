fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 100,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}


def main():
    fruit_input = input("Enter fruit name: ").strip().lower()
    if fruit_input in fruit_calories:
        print(f"Calories:{fruit_calories[fruit_input]}")


if __name__ == '__main__':
    main()
