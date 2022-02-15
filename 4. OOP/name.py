class Person:
    def __init__(self, name, birth_year, height):
        self.name = name
        self.birth_year = birth_year
        self.height = height
        
    def get_name(self):
        return self.name
    
    def get_birth_year(self):
        return self.birth_year
    
    def get_summary(self):
        return f"{self.name} was born in {self.birth_year} and is {self.height} tall."


first_person = Person("jhon", "", "")
print(first_person.get_name())

second_person = Person("Jane", 1980, 60)
print(second_person.get_summary())
