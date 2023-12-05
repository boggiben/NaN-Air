class Employee:
    def __init__(self, name="", national_id="", address="", gsm="", email=""):
        self.name = name
        self.national_id = national_id
        self.address = address
        self.gsm = gsm
        self.address = address
        self.email = email

    def __str__(self):
        return f"name: {self.name}, national id: {self.national_id}, address: {self.address}, mobile number: {self.gsm}, email: {self.email}"
