#!/usr/bin/env python3

def crackle_pop(num: int):
    crackle_popped = False
    if num % 3 == 0: 
        print("Crackle", end="")
        crackle_popped = True
    if num % 5 == 0: 
        print("Pop", end="")
        crackle_popped = True
    if not crackle_popped:
        print(num, end="")
    print() # print just a newline
    
        
if __name__ == "__main__":
    for i in range(1, 101): 
        crackle_pop(i)

