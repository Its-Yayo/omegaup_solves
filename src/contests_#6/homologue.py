#!/usr/bin/python3

def main():
    """ Code to determine if determine the side D of a triangle given sides A, B, and C."""

    a = int(input("Enter side A: "))
    b = int(input("Enter side B: "))
    c = int(input("Enter side C: "))

    d = (c * b) / a

    print(int(d))

if __name__ == "__main__":
    main()
