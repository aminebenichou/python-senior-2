import random
class Student():
    gpd = 10.00
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f'{self.name} {self.age}'
    
    def is_passed(self):
        if self.gpd >= 10 :
            return True


students = []
for item in range(0, 10):
    student = Student(name=str(item), age=25)
    gpd = random.randint(5,17)
    student.gpd = gpd
    info = {
        'age' : student.age,
        'name': student.name,
        'gpd': student.gpd
    }
    if student.is_passed() :
        students.append(info)

print(students)

