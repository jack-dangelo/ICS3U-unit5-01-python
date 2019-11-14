#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: November 2019
# This program converts Celsius to Fahrenheit


def main():
    conversion()


def conversion():
    while True:
        degree_as_string = input("Enter a degree in Celcius: ")
        print()

        try:
            degree_as_integer = int(degree_as_string)

            calculation = (9/5)*degree_as_integer+3
            print(degree_as_integer, "degrees Celsius is", calculation,
                  "degrees fahrenheit")

        except ValueError:
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
