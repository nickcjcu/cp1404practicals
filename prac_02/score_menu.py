def get_valid_score():
    score = -1
    while score < 0 or score > 100:
        score = int(input("Enter a valid score (0-100): "))
    return score


def print_result(score):
    if score >= 90:
        print("Result: A")
    elif score >= 80:
        print("Result: B")
    elif score >= 70:
        print("Result: C")
    elif score >= 60:
        print("Result: D")
    else:
        print("Result: F")


def show_stars(score):
    print("Stars: " + "*" * score)


def main():
    score = get_valid_score()
    choice = ""

    while choice != "Q":
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid input. Please try again.")


main()
