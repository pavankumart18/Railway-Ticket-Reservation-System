class Person:
    def __init__(self, name, age, gender):
        # The constructor method initializes the attributes name, age, and gender for the Person instance
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        # This method returns a string representation of the Person instance
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}"

# Demonstration
# Create an instance of the Person class with name "John", age 30, and gender "Male"
# P = Person("John", 30, "Male")
# Print the string representation of the Person instance
# print(P)
