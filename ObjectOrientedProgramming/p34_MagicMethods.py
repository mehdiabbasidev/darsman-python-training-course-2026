class ShopingCart:
    def __init__(self,shoping_id:int,customer_name:str):
        self.shoping_id=shoping_id
        self.customer_name=customer_name
        self.items=[]

    def add_item(self,item:str):
        self.items.append(item)


    def __str__(self):
        temp=f"Shoping Id : {self.shoping_id}\nCustomer Name : {self.customer_name}\n"
        temp+=f"Items: {self.items}"
        temp+=f"\n{70*"-"}"
        return temp
    
    def __repr__(self):
        return f"ShopingCart({self.shoping_id},'{self.customer_name}',{self.items})"
    
    def __eq__(self, obj2):                             # ==
        return self.items == obj2.items
    

    def __add__(self, obj2):                            # +
        new_shopcart=ShopingCart(300,'Sara')
        new_shopcart.items=self.items+obj2.items
        return new_shopcart

    def __len__(self):                                  # len
        return len(self.items)
# --------------------------------------------------------------
s1=ShopingCart(1,"mehdi")
s1.add_item("CPU")
s1.add_item("RAM")
s1.add_item("VGA")
print(s1)

s2=ShopingCart(1000,"ahmad")
s2.add_item("labtop")
s2.add_item("mobile")
print(s2)



print(len(s1))
print(len(s2))









# s1=ShopingCart(1,"mehdi")
# s1.add_item("CPU")
# s1.add_item("RAM")
# s1.add_item("VGA")
# print(s1)

# s2=ShopingCart(1000,"ahmad")
# s2.add_item("labtop")
# s2.add_item("mobile")
# print(s2)


# s3=s1+s2
# print(s3)








# s1=ShopingCart(1,"mehdi")
# s1.add_item("CPU")
# s1.add_item("RAM")
# s1.add_item("VGA")
# print(s1)


# s2=ShopingCart(2,"ali")
# s2.add_item("CPU")
# s2.add_item("RAM")
# print(s2)

# print(s1==s2)






# s1=ShopingCart(1,"mehdi")
# s1.add_item("CPU")
# s1.add_item("RAM")
# s1.add_item("HDD")
# print(s1)

# s2=ShopingCart(1000,"ahmad")
# s2.add_item("labtop")
# s2.add_item("mobile")
# print(s2)



# s1.add_item("VGA")
# print(repr(s1))
