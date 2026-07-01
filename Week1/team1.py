num = int(input("Please enter a number: "))

def main():
    print("Start Here")
    print(num)

    user = str(input("Choose one of the following: \nSquaring, Cubing, Square Rooting "))

    if(user == "Squaring"):
        square()
    
    if(user == "Cubing"):
        cube()


def square():
   sq = num * num 
   print(sq)

square()

def cube():
    cub = num * num * num
    print(cub)
    
cube()

main()

