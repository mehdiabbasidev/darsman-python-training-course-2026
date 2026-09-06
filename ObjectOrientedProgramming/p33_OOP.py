class Student:
    def __init__(self,name,family,st_id,phone):
        self.name=name
        self.family=family
        self.st_id=st_id
        self.phone=phone

    def register(self):
        pass

    def print_info(self):
        print(f"Name : {self.name}\tFamily : {self.family}")

    def __str__(self):
        return f"Name: {self.name}\t\tFamily: {self.family}\nPhone: {self.phone}\t\tStudent Id: {self.st_id}\n{80*"-"}"
    
#-----------------------------------------------------------
s1=Student('mehdi','abbasi',1234,'0912000000')
s2=Student('ali','rezaie',44444,'0913000000')
s3=Student('sara','ahmadi',2222,'0914999999')
s1000=Student('ahmad','mohammadi',5555,'0916999999')

# s1.print_info()
# s3.print_info()
# s1000.print_info()


print(s1)
print(s2)
print(s3)
print(s1000)