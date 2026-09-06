class User:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email
        self.__password=password

    def get_password(self):
        return self.__password

    def set_password(self,new_apss):
        self.__password=new_apss

# ----------------------------------------------
u1=User('mehdi','mehdi@gmail.com','123456')

print(u1.get_password())
u1.set_password("111111111111111111")
print(u1.get_password())









