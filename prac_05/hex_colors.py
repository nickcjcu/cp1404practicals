COLOR_TO_HEX = {
    "Frostbite": "#e936a7",
    "Fuchsia Purple": "#cc397b",
    "Fuchsia Rose": "#c74375",
    "Fulvous": "#e48400",
    "Fuzzy Wuzzy": "#87421f",
    "GO Green": "#00ab66",
    "Gainsboro": "#dcdcdc",
    "Gamboge": "#e49b0f",
    "Generic Viridian": "#007f66",
    "GhostWhite": "#f8f8ff"
}

color_name = input("Enter color name: ").title()
while color_name != "":
    try:
        print(f"{color_name} has the hex code {COLOR_TO_HEX[color_name]}")
    except KeyError:
        print("Invalid color name")

    color_name = input("Enter color name: ").title()

print("Goodbye!")
