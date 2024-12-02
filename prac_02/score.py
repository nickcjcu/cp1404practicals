import random

def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")

def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()
