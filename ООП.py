class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет!"

    def hobby(self):
        return "У меня нет какого-либо хобби :("

class Student(Person):
    def greet(self):
        return f"Я студент, меня зовут {self.name}, мне {self.age} лет!"

    def hobby(self):
        return "Я изучаю Python :)"

class Teacher(Person):
    def greet(self):
        return f"Я преподаватель, меня зовут {self.name}, мне {self.age} лет!"
    def hobby(self):
        return "Я занимаюсь научной работой в свободное время :)"

person = Person("Александр", 18)
student = Student("Женя", 19)
teacher = Teacher("Павел", 30)

for p in (person, student, teacher):
    print(p.greet())
    print(p.hobby())
    print()
