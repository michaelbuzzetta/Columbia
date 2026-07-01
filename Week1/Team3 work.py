#modifications made by Team1

def show_answer(text):
    print("\n\n\n\n")
    print("\033[1;32m" + text + "\033[0m")
    print("\n\n\n\n")


def main():
    burger_price = 6.00
    pizza_price = 5.00
    hotdog_price = 4.00
    taco_price = 3.00

    while True:
        Ctype = input(
            "Which food would you like, or type stop to quit? Use number to order:\n"
            "1. Burger\n"
            "2. Pizza\n"
            "3. Hotdog\n"
            "4. Taco\n"
        ).strip().lower()

        if Ctype == "stop":
            break

        elif Ctype == "1" or Ctype == "burger":
            show_answer(f"The burger costs ${burger_price + {burger_price * 0.025}}")

        elif Ctype == "2" or Ctype == "pizza":
            show_answer(f"The pizza costs ${pizza_price + {pizza_price * 0.025}}")

        elif Ctype == "3" or Ctype == "hotdog":
            show_answer(f"The hotdog costs ${hotdog_price + {hotdog_price * 0.025}}")

        elif Ctype == "4" or Ctype == "taco":
            show_answer(f"The taco costs ${taco_price + {taco_price * 0.025}}")

        else:
            print("Please try again.")


main()
