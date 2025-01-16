#how to calculate the squre root of any number ??
#MOHAMMAD SHUJAULLAH(22BEE028)
#Solution-1(using exponensiation)

n=28
sqrt=n**(1/2)
print("the square root of the numis ",sqrt)

# solution -2 (using math library)
import math
num=int(input("enter the value of no."))
sr=math.sqrt(num)
print("the sqr root of no. is ",sr)



#calculate squareroot of complex and negative no.??
import cmath
num=complex(2,3)
num_sqrt=cmath.sqrt(num)
print("the square root of no. is{num}",num_sqrt)



# calculate the area of a triangle 
b=float(input("enter the value of base "))
h=float(input("enter the value of height"))
area=1/2*b*h
print("area of the triangle is ",area,"m")
