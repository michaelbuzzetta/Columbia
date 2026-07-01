def main():
    print("Start Here")
    try:
        current_time=int(input("What time is it? Set a number from 1-24 hours"))
        if (current_time <= 12 and current_time>=4):
            print("Good Morning")
        elif(current_time <19  and current_time>12):
            print("Good Afternoon")
        elif(current_time <=24  and current_time>19):
            print("Good Night")
        elif(time > 24 and time < 1):
    except ValueError as e:
        print("Invalid Input.")

    
main()