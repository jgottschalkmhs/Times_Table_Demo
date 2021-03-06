# Integer checking function


# Number checking function goes here
def int_check(question, low=None, high=None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


def instructions():
    print("Choose the times table you want to generate.")
    print()
    print("Choose how high you want to go.")
    print()
    return ""


def yes_no(question):
    valid = False
    while not valid:
        response = input(question)
        
        if response == "y" or response == "yes":
            return response
        elif response == "n" or response == "no":
            return response
        else:
            print("Please enter yes / no")


# Main routine

show_instructions = input("Have you used this program before? ").lower()

if show_instructions == "no":
    instructions()

# Get input
table = int_check("Which times table? ", 1)
how_high = int_check("How high? ", 1)

# output via a loop
for item in range(1, how_high + 1):
    times_table = "{} × {} = {}"\
        .format(item, table, item * table)
    print(times_table)

print("Thanks for using my program")
