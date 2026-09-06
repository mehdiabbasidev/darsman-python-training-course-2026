class User:
    count=0

    def __init__(self,name,family):
        self.name=name
        self.family=family
        User.count+=1
    
    def welcom(self):
        print(f"Hello {self.name}")

    
    @classmethod
    def show_count(cls):
        print(f"Count is : {cls.count}")


    @staticmethod
    def is_valid_name(name):
        return len(name)>=3


    



user1=User('mehdi','abbasi')
user2=User('ali','rezaie')
user3=User('ahmad','mohammadi')

user1.welcom()

User.show_count()

print(User.is_valid_name("a"))
print(User.is_valid_name("mehdi"))
print(User.is_valid_name("rt"))
print(User.is_valid_name("rsdfjshgd"))