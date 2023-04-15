#!/usr/bin/python3

""" Code to square an arg number until it reaches 65536. 
    Outputs the squared number and the number of iterations. """

def main():
    n = int(input("Enter a number: "))
    i = 0

    if n >= 2 and n <= 1000000: 
        while n < 30000:
            n *= n
            i += 1  
        
        print(n, i)

if __name__ == "__main__":
    main()
