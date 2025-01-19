import random

# Trivia game
# QUESTIONS TO ASK
user_name = input("What is your name? ")

question_0 = input("Are you ready to play a trivia game? (yes/no): ")

if question_0.lower() == "yes":
    print(f"Great! Let's get started, {user_name}!")
    
    score = 0  # Initialize score

    question_1 = input("Who is the first president of the United States? ")
    if question_1.lower() == "george washington":
        print("Correct!")
        score += 1
    else:
        print("Sorry, that's incorrect.")
    
    question_2 = input("What is the capital of France? ")
    if question_2.lower() == "paris":
        print("Correct!")
        score += 1
    else:
        print("Sorry, that's incorrect.")
    
    question_3 = input("What is the largest mammal in the world? ")
    if question_3.lower() == "blue whale":
        print("Correct!")
        score += 1
    else:
        print("Sorry, that's incorrect.")
    
    question_4 = input("What is the largest planet in our solar system? ")
    if question_4.lower() == "jupiter":
        print("Correct!")
        score += 1
    else:
        print("Sorry, that's incorrect.")
    
    question_5 = input("What is the smallest planet in our solar system? ")
    if question_5.lower() == "mercury":
        print("Correct!")
        score += 1
    else:
        print("Sorry, that's incorrect.")
    
    print(f"{user_name} has gotten {score} out of 5 points.")
    
elif question_0.lower() == "no":
    print("That's okay! Let me know when you're ready.")
else:
    print("Please enter 'yes' or 'no' to continue.")