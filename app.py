

""" count = 1

while count <= 5:
    print("This is loop number", count)
    count = count + 1
 """
""" order = ""

while order != "done":
    order = input("What would you like to order? (type 'done' to finish): ")

print("Thanks for your order!") """

""" count = 10
while count >=1:
    print("This is loop number", count)
    count = count-1 """

""" favorite_color = ""

while favorite_color != "Stop":
    favorite_color = input("What is your favorite color? (Type 'stop' to finish):")
print("Okay") """

# Number Guessing Game

import random
random_int = random.randint(1,10)
guess_num = 0

while guess_num != random_int:
    guess_num = int(input("Guess a random number from 1-10(Inclusive)"))
    if guess_num > random_int:
        print(f"{guess_num} is greater than the number")
        guess_history = ["Guess History:"]
        for i in range(i):
            guess_history.append(guess_num)
    elif guess_num == random_int:
        print("You Guessed Correctly")
    else:
        print(f"{guess_num} is less than the number")
        guess_history = ["Guess History:"]
        for i in range(i):
            guess_history.append(guess_num)


print(guess_history)
