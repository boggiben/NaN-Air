from logic.logic_wrapper import LogicWrapper
from logic.staff_logic import Staff_Logic
from model.employee import Employee


class Staff_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("--Starfsmenn--")
        print("1. Sjá alla starfsmenn")
        print("2. Skrá nýjan starfsmann")
        print("3. Sjá lausa starfsmenn")
        print("4. Sjá upptekna starfsmenn")
        print("b. Til að fara í aðalvalmynd")

    def input_staff_menu(self):
        while True:
            self.menu_output()
            user_input = input("Veldu aðgerð: ")
            if user_input == "1":
                print("Þú valdir að sjá alla starfsmenn")
                result = self.logic_wrapper.get_all_staff()

                for elem in result:
                    print(
                        f"name: {elem.name}, mobile_number: {elem.mobile_number}, email: {elem.email}, address: {elem.address}, national_id: {elem.national_id}, role: {elem.role}"
                    )

            elif user_input.lower() == "2":
                print("Þú valdir að skrá nýjan starfsmann")
                success = self.add_new_staff_ui()
                if success:
                    print("Aðgerð tókst!")
            elif user_input.lower() == "b":
                break
            else:
                print("Rangur innsláttur. Reyndu aftur.")


    def add_new_staff_ui(self):
        new_employee = Employee()
        name = input("Nafn: ")
        new_employee.name = name
        national_id = input("Kennitala: ")
        new_employee.national_id = national_id
        address = input("Heimilisfang: ")
        new_employee.address = address
        mobile_number = input("Símanúmer: ")
        new_employee.mobile_number = mobile_number
        email = input("Netfang: ")
        new_employee.email = email
        role = input("Staða: ")
        new_employee.role = role
        return self.logic_wrapper.add_new_staff(new_employee)