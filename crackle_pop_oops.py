#!/usr/bin/env python3

def sum_digits(num_str: str): 
    res = 0 
    for digit in num_str:
        res = res + int(digit)
    return res

#Recursively sum digits until the result is 0-9 
def recursively_sum_digits(num_str: str): 
    num_str = sum_digits(num_str)
    num = int(num_str)
    if num < 10:  
        return num
    else: 
        return recursively_sum_digits(str(num))

def crackle_pop(num_str: str):
    if recursively_sum_digits(num_str)

def main():
    num_str = input("Please enter a number. If it's divisible by 3, I'll print Crackle. If it's divisible by 5, I'll print Pop.\n")
    try:
        num = abs(float(number_string)) #gently sidestepping handling "-" in negative numbers
    except ValueError: 
        print("Dude, number. Plz enter a number.")
    if num.is_integer():
        crackle_pop(str(int(num)))
    else:
        print("The number you gave is not an integer, and so can't be divisible by 3 or 5")
    
        
if __name__ == "__main__":
    main()


