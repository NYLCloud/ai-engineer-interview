class User:
    def __init__(self, name, email, age, department):
        self.name = name
        self.email = email
        self.age = age
        self.department = department

def create_user_dict(name, email, age, department):
    return {
        "name": name,
        "email": email,
        "age": age,
        "department": department
    }

def validate_email(email):
    return "@" in email