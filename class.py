class Student:
    def __init__(self, name,student_no, course):
        self.name=name
        self.student_no=student_no
        self.course=course

    def study(self,unit):
        print(f"{self.name} studies {unit}")

    def run(self,marathon):
        print(f"{self.name} runs {marathon}")

    def code(self,time):
        print(f"{self.name} codes at {time}")

    def get_details(self):
        print("User details")
        print(f"Name:{self.name} - Student No:{self.student_no} - Course:{self.course}")
        print("-------------------------")


# very direct method
# object1
student1=Student("Jack","S101","Computer Science")
print(type(student1))
student1.get_details()
print(student1.name)
print(student1.student_no)
print(student1.course)
student1.study("Computer Science")
student1.run("Olympics")
student1.code("9pm")

# object2
student2=Student("Jane","S102","Data Science")
print(type(student2))
student2.get_details()
print(student2.name)
print(student2.student_no)
print(student2.course)
student2.study("Data Science")
student2.run("Kenya Marathon")
student2.code("5am")


