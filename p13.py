
## for print ascii value of a charrecter 
# SHVAIB KHAN(22BEE035)

print("enter a string :",end="")
text=input()

textlength=len(text)
print("length of the string is ",textlength)


for char in text:
    ascii=ord(char)
    print(char,"\t",ascii)
