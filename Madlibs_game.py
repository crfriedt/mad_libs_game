import random

# ***** Mad Libs Game *****

# A list of madlibs

madLibs = [
    "It was Thanksgiving and the scent of succulent roast wafted through my house. it's time to ! my mother called. I couldn't wait to get my on that Thanksgiving meal. My family sat around the dining-room . The table was laid out with every kind of imaginable. There was a basket of hot buttered and glasses of sparkling . The turkey sat, steaming, next to a tureen of gravy. A bowl of ruby-red sauce, a sweet- casserole, and a dish of mashed tempted my taste buds. But the dish I looked forward to most was Grandma 's famous pie. Thanksgiving is my favorite holiday, down.",
    "It's simple. Turn the . Make him/her want to date you. Make sure you're always dressed to . Each and every day, war a/an that you know shows off your to advantage and make your look like a million . Even if the two of you make meaningful contact, don't admit it. No hugs or . Just shake his/her firmly. And remember, when he/she asks you out, even though a chill may run down your and you can;t stop your from . Just play it . Take a long pause before answering in a very voice. I'll have to it over.",
]

# Generate a random number depending on size of madLibs list

randomIndex = random.randint(0, len(madLibs) - 1)

# Ask user for inputs depending on random madLib, split string in to list, slice user inputs in to list, join list to string.

if randomIndex == 0:
    print("Mad Lib: What's for dinner?\n")

    splitString = madLibs[0].split()

    nounOne = input("noun: ")
    splitString.insert(9, nounOne)

    personInRoom = input("person in room: ")
    splitString.insert(14, personInRoom)

    verbOne = input("verb: ")
    splitString.insert(18, verbOne)

    partOfBodyOne = input("part of the body (plural): ")
    splitString.insert(29, partOfBodyOne)

    adjectiveOne = input("adjective: ")
    splitString.insert(32, adjectiveOne)

    nounTwo = input("noun: ")
    splitString.insert(41, nounTwo)

    nounThree = input("noun: ")
    splitString.insert(52, nounThree)

    pluralNounOne = input("plural noun: ")
    splitString.insert(61, pluralNounOne)

    typeOfLiquid = input("type of liquid: ")
    splitString.insert(66, typeOfLiquid)

    adjectiveTwo = input("adjective: ")
    splitString.insert(69, adjectiveTwo)

    nounFour = input("noun: ")
    splitString.insert(78, nounFour)

    nounFive = input("noun: ")
    splitString.insert(84, nounFive)

    nounSix = input("noun: ")
    splitString.insert(88, nounSix)

    pluralNounTwo = input("plural noun: ")
    splitString.insert(95, pluralNounTwo)

    personInRoomFemale = input("person in room (female): ")
    splitString.insert(110, personInRoomFemale)

    nounSeven = input("noun: ")
    splitString.insert(113, nounSeven)

    partOfBodyPlural = input("part of the body (plural): ")
    splitString.insert(120, partOfBodyPlural)

    joinedString = " ".join(splitString)
    print("\n",joinedString)


elif randomIndex == 1:
    print("Mad Lib: How to date the coolest guy/girl in school")
    splitString = madLibs[1].split()
