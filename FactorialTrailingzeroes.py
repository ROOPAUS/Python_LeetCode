#To find factorial of a number and to find the trailing zeros in that factorial

def factorial(n):
    if (n==1 or n==0): 
        return 1 
    else: 
        return  n * factorial(n-1)

def trailingZeroes(factorial):
    temp = factorial
    count = 0
    while(temp>=10):
        if ((temp % 10)==0):
            count +=1
            temp = temp/10
        else :
            temp = temp/10
    return count 

#Driver code
num = int(input("Enter number: "))
print("factorial of", num,"is", factorial(num))
print("The number of trailing zeroes in", factorial(num),"is",trailingZeroes(factorial(num)))

#Another method to find trailing zeroes(recommended)

def findZeroes(num):
    i=5
    count = 0
    while(int(num/i)>=1):
        count += int(num/i)
        i *= 5
    return count

print("The trailing zeroes in factorial of", num, "is", findZeroes(num))



   