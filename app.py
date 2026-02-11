

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
print(random_int)
guess_num = int(input("Guess a random number from 1-10"))

while guess_num != random_int:
    if guess_num != random_int:
        guess_history = [guess_num]
        if guess_num > random_int:
            print("Number is less than")
    
        else:
            print("Number is greater than")
    print(guess_num)
print("You Guessed Correctly")

