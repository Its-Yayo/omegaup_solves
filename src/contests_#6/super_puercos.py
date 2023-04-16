#!/usr/bin/python3

def main():
    """ Code to determine which names will be graduated. 
        Only one init alphabet is allowed. 
        
        Test case example:
        Input -> 5 okja porky petunia babe peggy
        Output -> 3 """

    n = int(input())
    puercos = []

    for i in range(0, n):
        animals = input().strip().lower()
        letter = animals[0]

        if letter not in [p[0] for p in puercos]:
            puercos.append(animals)
    
    final = len(puercos)
    print(final)

if __name__ == '__main__':
    main()