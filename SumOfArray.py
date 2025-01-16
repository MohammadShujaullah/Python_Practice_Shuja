# python program to find sum of an aaray
# MD SHAHNWAJ(22BEE026)
lst=[]
# number of element as input
n=int(input("enter the value of element:"))
for i in range (n):
    ele=int(input())
    lst.append(ele)

print(lst)    

sum=0
for i in range (n):
    sum=sum+lst[i]
print(sum)  