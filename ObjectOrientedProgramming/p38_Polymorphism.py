from datetime import datetime

# ----------------------------------------------------------------
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age    

    def get_birth_year(self):
        current_year=datetime.now().year
        return f"Birth Year : {current_year-self.age}"
    
    def get_info(self):
        return f"Name : {self.name}\t\t\tAge : {self.age}\n"

    def test(self):
        print("Person...")


# ----------------------------------------------------------------
class Student(Person):
    def __init__(self,st_id,name,age):
        super().__init__(name,age)
        self.st_id=st_id

    def study(self):
        return "Stuedent is studying"
    
    def get_info(self):
        return f"{super().get_info()}st_id : {self.st_id}"

    def test(self):
        super().test()
        print("Student...")   
# ----------------------------------------------------------------
class Teacher(Person):
    def __init__(self,t_code,department,name,age):
        super().__init__(name,age)
        self.t_code=t_code
        self.department=department

    def teach(self):
        return "Teacher is teaching"
    
    def get_info(self):
        return f"{super().get_info()}t_code : {self.t_code}\t\tdepartment : {self.department}"       

    def test(self):
        super().test()
        print("Teacher...")
# ----------------------------------------------------------------
class Employee(Person):
    def __init__(self,p_code,hire_year,name,age):
        super().__init__(name,age)
        self.p_code=p_code
        self.hire_year=hire_year

    def work(self):
        return "Employee is working"
    
    def get_info(self):
        return f"{super().get_info()}p_code : {self.p_code}\nhire_year : {self.hire_year} \n{80*"#"}"   

    def test(self):
        super().test()
        print("Employee...")
# ----------------------------------------------------------------
s1=Student(1234,"ali",21)
t1=Teacher(1000,"Computer","mehdi",45)
e1=Employee(44444,2005,"hamed",47)

people=[s1,t1,e1]

for person in people:
    print(person.get_info())




# t1.test()

