'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
1. Write an Employee class with an __init__ method that stores three
   instance variables: name, title, and salary.
2. Create two Employee objects and assign any values you like.
3. Print each employee's details in the format:
   Name: <name>, Title: <title>, Salary: <salary>
'''

class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
        pass
    
emp1 = Employee("Bob Gardner", "Project Manager", 150000)
emp2 = Employee("Rob Farmer", "Product Manager", 120000)

print(f"Name: {emp1.name}, Title: {emp1.title}, Salary: {emp1.salary}")
print(f"Name: {emp2.name}, Title: {emp2.title}, Salary: {emp2.salary}")