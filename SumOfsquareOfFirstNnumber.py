## 14.PYTHON PROGRAM FOR SUM OF SQUARES OF FIRST n NATURAL NUMBERS
 

def  squaresum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
    return sum


n=3
print(" THE SUM OF N NATURAL NUMBER IS =",squaresum(n))
