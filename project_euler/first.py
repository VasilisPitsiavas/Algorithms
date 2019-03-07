def calculate(a,N):
    n = N/a
    y = n *(n+1) / 2
    sum = a*y
    return sum

z = calculate(3,1000)
d = calculate(5,1000)
f = calculate(15,1000)
k = z+d-f
print k
print("So the sum of all multiplies of 3 and 5 below 1000 is " ,k )
