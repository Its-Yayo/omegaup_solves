#!/usr/bin/python3

def main():
    """ Code to square an arg number until it reaches 30000. 
    Outputs the squared number and the number of iterations. 
    
    Test case example:
    Input -> 2
    Output -> 65536 4 """

    n = int(input())
    i = 0

    if n >= 2 and n <= 1000000: 
        while n < 30000:
            n *= n
            i += 1 

            if n == 30000:
                break 
        
        print(n, i)

if __name__ == "__main__":
    main()
