#!/usr/bin/python3

def main():
    """ Code to determine which user (Juan or Pedro) has 
        more money. Juan recieves 3 coins and Pedro 2. (In this order)
        
        Test case example:
        Input -> 10 5 2 10 10 
        Output -> Pedro """

    juan = [int(input()) for i in range(0, 3)]
    pedro = [int(input()) for i in range(0, 2)]

    sum_juan = sum(juan)
    sum_pedro = sum(pedro)

    print("Juan") if sum_juan > sum_pedro else print("Pedro")

if __name__ == '__main__':
    main()