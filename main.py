# Louqman was here.

Y10EnglishQuestions = {"Question":"Answer",
                       "Question2":"Answer2"}

from datetime import datetime

def Revise():
    while True:
        yearGroup = int(input("What year group would you like to revise? "))
        if yearGroup == 9:
            Year9Subjects()
        elif yearGroup == 10:
            Year10Subjects()
        elif yearGroup == 11:
            Year11Subjects()
        elif yearGroup < 9 or yearGroup >11:
            print("Error! Please provide a year group between 9 and 11!")


def Year9Subjects():
    print()
    print("1: English")

def Year10Subjects():
    pass

def Year11Subjects():
    pass

print(f"The time now is: {datetime.now()}")