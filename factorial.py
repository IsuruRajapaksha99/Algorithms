
#function to calculate factorial
def factorial(n):
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))

print(factorial(50))

def facto(n):
    if n<=1:
        return 1
    else:
        x=1
        for i in range(0,n):
           x=x+x*i
        
        return x

print(facto(10))