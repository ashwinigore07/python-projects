import random
secret = random.randint(1,100)
while True:
    guess = int(input("Guess the number "))
    if guess < secret:
       print("Too low!")
    elif guess > secret:
      print("TOO high")
    else:
      print("correct")
      break
