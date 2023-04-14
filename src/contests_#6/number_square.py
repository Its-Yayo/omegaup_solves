#!/usr/bin/python3

""" Code to square an arg number until it reaches 65536. 
    Outputs the squared number and the number of iterations. """

def solution(n: int) -> int:
    i = 0

    while n < 65536:
        n = n ** 2
        i += 1

        if (n == 65536):
            break

    return n, i

def main():
    n = int(input("Enter a number: "))
    print(solution(n))

if __name__ == "__main__":
    main()