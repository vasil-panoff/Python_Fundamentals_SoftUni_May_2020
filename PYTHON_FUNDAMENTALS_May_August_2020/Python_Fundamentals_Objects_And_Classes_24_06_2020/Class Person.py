class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

me = Person("Vasil", "Panov", 42)
me.age +=1
print(me.first_name)  # Peter
print(me.last_name)  # Johnson
print(me.age)  # 25