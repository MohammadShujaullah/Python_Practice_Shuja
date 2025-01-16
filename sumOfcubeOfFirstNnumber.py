#PYTHON PROGRAM FOR CUBE SUM OF FIRST  N NATURAL NUMBERS
 
def  cubesum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i*i)
    return sum


n=3
sum=cubesum(n)
print(" THE CUBE SUM OF N NATURAL NUMBER=",sum)
