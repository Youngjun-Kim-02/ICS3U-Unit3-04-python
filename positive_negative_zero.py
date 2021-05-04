#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program checks if integer is positive or negative or zero


def main():
    # this function checks if integer is positive or negative or zero

    # input
    integer = int(input("Enter an integer: "))
    print("")

    # process & output
    if integer > 0:
        print("Positive number")
    elif integer == 0:
        print("0 is just zero")
    else:
        print("Negative number")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
