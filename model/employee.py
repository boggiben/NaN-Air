class Employee:
    def __init__(self, name="", gsm="", email="", address="", national_id="", role=""):
        self.name = name
        self.gsm = gsm
        self.email = email
        self.address = address
        self.national_id = national_id
        self.role = role

    def __str__(self):
        return f"Nafn: {self.name}, Farsími: {self.gsm}, Tölvupóstur: {self.email}, Heimilisfang: {self.address}, Kennitala: {self.national_id}, Staða: {self.role}"
