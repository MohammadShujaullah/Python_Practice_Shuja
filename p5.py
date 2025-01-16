# Python program for compound interest
# SHVAIB KHAN(22BEE035)
p=float(input("Enter principle amt:"))
r=float(input("Enter interest rate:"))
t=float(input("Enter time duration:"))
n=float(input("Number of times interest applied per time"))
compound_interest=p*((1+r/n))**(n*t)
print("The compound interest is: ",compound_interest)