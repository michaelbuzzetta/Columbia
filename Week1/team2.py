# this is a Time checker????????? idk Team 2 have 5 error with only 12 line of code QwQ

import math
def main():
    current_time = 0  

def checknumber(checker):
    while True:
        try:
            number = float(input(checker))

            if not math.isfinite(number):
                print("Please enter a valid number.")
                continue
            return number
        except ValueError:
            print("Please enter a valid number.")  
def show_answer(text):
    print("\n\n\n\n")
    print("\033[1;32m" + text + "\033[0m")
    print("\n\n\n\n")
while True:
        current_time = checknumber("What time is it? Set a number from 1-24 hours: ")
        if (current_time >= 4 and current_time <= 12):
            show_answer(f"Good Morning, it is {current_time} O'clock")

        elif(current_time > 12  and current_time <= 19):
            show_answer(f"Good Afternoon, it is {current_time} O'clock")

        elif(current_time > 19 and current_time <= 24):
            show_answer(f"Good Nigh, it is {current_time} O'clockt")

        elif(current_time > 0 and current_time < 4):
            show_answer(f"Good Night, it is {current_time} O'clock")
        else: 
            print(f"Please enter a valid number.")