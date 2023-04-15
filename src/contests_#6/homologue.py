#!/usr/bin/python3

def main():
    """ Code to determine if determine the side D of a triangle given sides A, B, and C."""

    a = int(input())
    b = int(input())
    c = int(input())

    d = (b / a) * c

    print(int(d))

if __name__ == "__main__":
    main()
