#Task 1: Calculate Factorial Using a Function 

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

i=int(input("Enter a number: "))
print(f"Factorial of {i} is : {fact(i)}")