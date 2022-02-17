'''
author = Dominik Strnad
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
line = "-" * 45
clean_text = []
numeric_list = []
count_words = 0
count_title = 0
count_upper = 0
count_lower = 0
count_numeric = 0
occurrence = {}

user = input("username: ")
password = input("password: ")
print(line)

if user in users and users[user] == password:
    print(f"Welcome to the app, {user}")
    print("We have 3 texts to be analyzed.")
    print(line)
    choice = input("Enter a number btw. 1 and 3 to select: ")
    print(line)

    if choice.isdigit():
        if int(choice) in range(1,4):
            text = TEXTS[int(choice) - 1].split()

            for word in text:
                clean_text.append(word.strip(",.;"))

            for word in clean_text:
                if word.istitle():
                    count_title = count_title + 1
                elif word.isupper():
                    count_upper = count_upper + 1
                elif word.islower():
                    count_lower = count_lower + 1
                elif word.isnumeric():
                    count_numeric = count_numeric + 1
                    numeric_list.append(int(word))

                if len(word) in occurrence:
                    occurrence[len(word)] = occurrence[len(word)] + 1
                else:
                    occurrence[len(word)] = 1

            count_words = (len(clean_text))
            numeric_sum = sum(numeric_list)

            print(f"There are {count_words} words in the selected text.")
            print(f"There are {count_title} titlecase words.")
            print(f"There are {count_upper} uppercase words.")
            print(f"There are {count_lower} lowercase words.")
            print(f"There are {count_numeric} numeric strings.")
            print(f"The sum of all the numbers {numeric_sum}")
            print(line)
            print("LEN|    OCCURRENCES     |NR.")
            print(line)

            for key, value in sorted(occurrence.items()):
                if key in range(10):
                    print(f"  {key}|{'*' * value}{' ' * (20-value)}|{value}")
                else:
                    print(f" {key}|{'*' * value}{' ' * (20-value)}|{value}")

        else:
            print("Input is not in range 1-3!")
            exit()
    else:
        print("Input is not integer!")
        exit()
else:
    print("Unregistered user, terminating the program...")
    exit()
