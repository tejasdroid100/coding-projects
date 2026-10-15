import random
random_number = random.randint(1,11)
secret_number = random_number
guess_count=0
guess_limit = 4
print("Welcome to the Guess Game. You have 4 tries, and the number is between 1 and 10")
while guess_count < guess_limit:
    guess = int(input("Guess the number"))
    guess_count += 1
    if guess==secret_number:
        print("!!!You guessed the number!!!")
        break
else:
    print("-______-You lost:(")
    print(f'The secret number was {secret_number}')