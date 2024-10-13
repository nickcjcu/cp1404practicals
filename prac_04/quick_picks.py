import random

NUMBERS = list(range(1, 46))

def main():
    quick_picks = int(input("How many quick picks? "))

    for _ in range(quick_picks):
        quick_pick = random.sample(NUMBERS, 6)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()