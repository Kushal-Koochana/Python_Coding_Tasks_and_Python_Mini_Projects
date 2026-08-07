print("Welcome to the guessing game. Guess the correct number to win.")
lower_bound = 1
upper_bound = 100
number_of_guesses = 0
answer = random.randint(lower_bound, upper_bound)
user_guess = input(
    f"Try guessing the positive integer between {lower_bound} and "
    f"{upper_bound} (type q to quit): "
)
user_guess = user_guess.strip().lower()

while user_guess != str(answer) and user_guess != "q":
    number_of_guesses += 1
    if not user_guess:
        print("Empty field entered, please retry.")
    elif not user_guess.isdigit():
        print("Enter a valid user input, please retry.")
    elif user_guess.isdigit() and (
        int(user_guess) < lower_bound or int(user_guess) > upper_bound
    ):
        print("Sorry out of range.")
    elif user_guess.isdigit() and int(user_guess) < answer:
        print("Sorry too low.")
    elif user_guess.isdigit() and int(user_guess) > answer:
        print("Sorry too high.")
    if user_guess != str(answer):
        user_guess = input(
            f"Try guessing the positive integer between {lower_bound} and "
            f"{upper_bound} again (type q to quit): "
        )
    user_guess = user_guess.strip().lower()
if user_guess == "q":
    print(f"You have quit the game, after {number_of_guesses} guesses")
if user_guess == str(answer):
    print(
        f"Congratulations you have guessed the number in {number_of_guesses} "
        "guesses"
    )
print("Thank you for playing the guessing game.")
