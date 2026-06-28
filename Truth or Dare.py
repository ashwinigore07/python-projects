import random

truth=[
    "What is your biggest fear",
    "Who is your bff"
]
Dare=[
    "Sing a Song",
    "DO 10 jumping jacks"
]

choice = input("Truth or Dare?").lower()

if choice == "truth":
    print(random.choice(truth))
else:
    print(random.choice(Dare))
