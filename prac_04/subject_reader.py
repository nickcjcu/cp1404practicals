"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    data = []  # Create an empty list to store the data
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n at the end of the line
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert number of students to an integer
        data.append(parts)  # Append each line's data (as a list) to the main list
    input_file.close()
    return data  # Return the list of lists


def display_subject_details(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
