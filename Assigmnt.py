##Q write a program that uses input to prompt a user for their name and then welcome them
name=(input("'please enter your  beautiful name '"))
print("welcome\n" +name+  "\ni am python and i want to invite you as a guest in my wedding ceremony  ")


##Q write aprogram to prompt the user for hours and rate per hour to compute gross pay
# use 35 hour s and rate 2.75 per hour to test the program (they pay should be 96.25)
hrs=float(input ('enter the hrs'))
rate =float(input('enter the value of rate '))
gross_pay=hrs*rate
print ('the gross pay is :',gross_pay)


##Q write a program which prompyt the user for celcius temperature ,converting the temperatue 
# to farenheit and print out the converted temperature
temp_incelcius=float(input('enter the value of temperature in celcius'))
farenheit=(9*temp_incelcius)/5+32
print(farenheit)

##Q  write aprogram that will accept number of passenger and distance from point 
#of origin to destination ,calculate the expenses of passenger idf the fare is p20.00
#per kilometer

no_passenger=int(input('ente the no of passenger '))
distance=100
fare=20
total_expenses=(fare*distance)*no_passenger
print(total_expenses,'are the total expenses')