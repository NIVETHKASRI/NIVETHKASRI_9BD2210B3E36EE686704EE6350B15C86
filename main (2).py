# 1.1 Implement a recursive function to calculate the factorial if a given number
import math
def fact(n):
    return(math.factorial(n))

num=int(input("Enter the number:"))
f=fact(num)
print("Factorial of",num,"is",f)
