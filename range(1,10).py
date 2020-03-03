#Luis Machuca
#2/28/2020
#This program check if the number is in range from 1,10.
#It will print out in inrange or not in range. 
def test_range(n):
    if n in range (1,10):
        print(" %s is in the range"%str(n))
    else:
        print("The number is outside the given range.")

n = input("Type in any number to check the range")
test_range(15)
