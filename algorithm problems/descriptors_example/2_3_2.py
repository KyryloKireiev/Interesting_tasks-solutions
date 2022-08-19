class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) is str and self.min_length <= len(string) <= self.max_length:
            return True
        return False


class StringValue:

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:

    login = StringValue(ValidateString())
    password = StringValue(ValidateString())
    email = StringValue(ValidateString())

    def __init__(self, login, password, email):

        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        lst = list()
        lst.append(self.login)
        lst.append(self.password)
        lst.append(self.email)

        return lst

    def show(self):

        form = f"<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>"

        return print(form)


form = RegisterForm("login", "password", "email")

print(form.get_fields())

form_2 = RegisterForm("lgsfg", "psfdg", "email_2")

print(form_2.get_fields())

form.show()
