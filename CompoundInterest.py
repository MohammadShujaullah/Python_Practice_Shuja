#PYTHON PROGRAM FOR COMPOUND INTEREST
# SHVAIB KHAN (22BEE035)

p=float(input('enter principle amount:'))
r=float(input('interest rate :'))
t=float(input('enter time duration :'))
n=float(input('number of times interest applied per time :'))

compund_interest =(p*(1+r/100)**t)-p
print("the compound interest is :",compund_interest)
 