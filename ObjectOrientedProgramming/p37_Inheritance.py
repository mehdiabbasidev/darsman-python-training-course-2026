from datetime import datetime

# ----------------------------------------------------------------
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age    

    def get_birth_year(self):
        current_year=datetime.now().year
        return f"Birth Year : {current_year-self.age}"
    
    def show_base_info(self):
        print(f"Name : {self.name}\tAge : {self.age}")


# ----------------------------------------------------------------
class Student(Person):
    def __init__(self,st_id,name,age):
        super().__init__(name,age)
        self.st_id=st_id

    def study(self):
        return "Stuedent is studying"
    
    def show_student_info(self):
        print(f"St Id : {self.st_id}")
        super().show_base_info()
        print(80*"-")
    
     
# ----------------------------------------------------------------
class Teacher(Person):
    def __init__(self,t_code,department,name,age):
        super().__init__(name,age)
        self.t_code=t_code
        self.department=department

    def teach(self):
        return "Teacher is teaching"
    
    def show_teacher_info(self):
        print(f"t_code : {self.t_code}\t\tdepartment : {self.department}")
        super().show_base_info()
        print(80*"-")
        


# ----------------------------------------------------------------
class Employee(Person):
    def __init__(self,p_code,hire_year,name,age):
        super().__init__(name,age)
        self.p_code=p_code
        self.hire_year=hire_year

    def work(self):
        return "Employee is working"
    

    def show_employee_info(self):
        print(f"p_code : {self.p_code}\t\thire_year : {self.hire_year}")  
        super().show_base_info()  
        print(80*"-")


# ----------------------------------------------------------------
s1=Student(1234,"ali",21)
t1=Teacher(1000,"Computer","mehdi",45)
e1=Employee(44444,2005,"hamed",47)


print(s1.get_birth_year())
print(t1.get_birth_year())
print(e1.get_birth_year())

print(80*"*")
print(s1.study())
print(t1.teach())
print(e1.work())

# print(80*"*")
# s1.show_base_info()
# t1.show_base_info()
# e1.show_base_info()


print(80*"*")
s1.show_student_info()
t1.show_teacher_info()
e1.show_employee_info()
