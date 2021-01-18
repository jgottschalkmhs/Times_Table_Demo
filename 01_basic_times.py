# basic times table generator

# Get input
table = int(input("Which times table? "))
how_high = int(input("How high? "))

# output via a loop
for item in range(0, how_high):
    times_table = "{} × {} = {}"\
        .format(item, table, item * table)
    print(times_table)
