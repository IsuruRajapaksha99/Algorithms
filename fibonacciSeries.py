
# fuction of the fibonacci Series
def fibonacciSeries(n):

    if n<= 1:
        return n
    else:
        return fibonacciSeries(n-1) + fibonacciSeries(n-2)

x=9
print(fibonacciSeries(x))

def fibo(n):
    a,b=0,1

    if n==0:
        return 0
    # loop should start from 1 because actual loop runs n+1 times
    else:
        for i in range(1,n):
            a,b=b,a+b
    
    return b

print(fibo(1))