secret_number = 12
guess = 0
while guess != secret_number:
    guess = int(input("enter your guess:"))
    if guess == secret_number:
        print("corrected! you gussed the number. ")
    else:
        print("wrong guess. try again!")

