import random 
print("Welcome to the Number Guess Game")
rand_number= random.randint(1,100)
print(rand_number)
attempts=0
while True:
    user_number= int(input("Enter a number between 1 to 100"))
    if user_number==rand_number:
        print ("great you guessed the correct number")
        attempts+=1
        print(f"You guessed the correct number in {attempts} attempts")
        break
    elif user_number>100 or user_number<1:
        print("please enter a number bettween given range")
        attempts+=1
    elif user_number>rand_number+5:
        print("you are near but above")
        attempts+=1
    elif user_number>rand_number-5:
        print("you are near but below")
        attempts+=1
    elif user_number<rand_number:
        print("Too low")
        attempts+=1
    else:
        print("Too high")
        attempts+=1
    
    
