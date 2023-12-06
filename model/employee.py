class Employee:
    def __init__(self, name="", gsm="", email="", address="", national_id="", role=""):
        self.name = name
        self.gsm = gsm
        self.email = email
        self.address = address
        self.national_id = national_id
        self.role = role

    def __str__(self):
        return f"name: {self.name}, mobile number: {self.gsm}, email: {self.email}, address: {self.address}, national id: {self.national_id}, role: {self.role}"
