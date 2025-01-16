class computer:
    def _init_(self):
        print('in init')
    def config(self):
        print("i5,16gb,1TB")
        print('i am in config')



c1=computer()                   ### comp is clled instance and process called instantiation
c2=computer()

print(type(c1))
print(computer.config(c1))      ## both are same 
print(c1.config())               ## both are same 
print(c1._init_())




 