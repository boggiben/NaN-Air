from logic.logic_wrapper import LogicWrapper
from logic.staff_logic import Staff_Logic
from model.employee import Employee


class Staff_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("\n----STARFSMENN----")
        print("1. Allir starfsmenn")
        print("2. Allir flugmenn")
        print("3. Allir flugþjónar")
        print("4. Skrá starfsmann")
        print("5. Finna starfsmann (nota kt) ")
        print("6. Breyta starfsmannaupplýsingum (nema nafni og kt)")
        print("7. Lausir starfsmenn (á eftir að útfæra)")
        print("8. Uppteknir starfsmenn (á eftir að útfæra)")
        print("b. Fara í aðalvalmynd")

    def input_staff_menu(self):
        while True:
            self.menu_output()
            user_input = input("Veldu aðgerð: ")
            if user_input == "1":
                print("Þú valdir að sjá alla starfsmenn")
                result = self.logic_wrapper.get_all_staff()

                for elem in result:
                    print(
                        f"Nafn: {elem.name:<10} | "
                        f"Símanúmer: {elem.gsm:<10} | "
                        f"Netfang: {elem.email:<20} | "
                        f"Heimilisfang: {elem.address:<20} | "
                        f"Kennitala: {elem.national_id:<20} | "
                        f"Staða: {elem.role:<10}"
                    )
            elif user_input == "2":
                print("Þú valdir að sjá alla flugmenn")
                result = self.logic_wrapper.get_all_pilots()

                for elem in result:
                    print(
                        f"Nafn: {elem.name:<10} | "
                        f"Símanúmer: {elem.gsm:<10} | "
                        f"Netfang: {elem.email:<20} | "
                        f"Heimilisfang: {elem.address:<20} | "
                        f"Kennitala: {elem.national_id:<20} | "
                        f"Staða: {elem.role:<10}"
                    )
            elif user_input == "3":
                print("Þú valdir að sjá alla flugþjóna")
                result = self.logic_wrapper.get_all_flight_attendants()

                for elem in result:
                    print(
                        f"Nafn: {elem.name:<10} | "
                        f"Símanúmer: {elem.gsm:<10} | "
                        f"Netfang: {elem.email:<20} | "
                        f"Heimilisfang: {elem.address:<20} | "
                        f"Kennitala: {elem.national_id:<20} | "
                        f"Staða: {elem.role:<10}"
                    )

            elif user_input.lower() == "4":
                print("Þú valdir að skrá nýjan starfsmann")
                success = self.add_new_staff_ui()
                if success:
                    print("Aðgerð tókst!")

            elif user_input.lower() == "5":
                ssn = input("kennitala: ")

                # Tökum við bæði kennitölu án og með bandstriki
                if "-" not in ssn and len(ssn) == 10:
                    ssn = ssn[:6] + "-" + ssn[6:]

                # print("upplýsingar")
                emp = self.logic_wrapper.get_employee_by_ssn(ssn)

                if emp is None:
                    print("Starfsmaður er ekki til")
                else:
                    print(emp)

            elif user_input.lower() == "b":
                break
            else:
                print("Rangur innsláttur. Reyndu aftur.")

    def add_new_staff_ui(self):
        new_employee = Employee()
        name = input("Nafn: ")
        new_employee.name = name
        mobile_number = input("Símanúmer: ")
        new_employee.mobile_number = mobile_number
        email = input("Netfang: ")
        new_employee.email = email
        address = input("Heimilisfang: ")
        new_employee.address = address
        national_id = input("Kennitala: ")
        new_employee.national_id = national_id
        role = input("Staða: ")
        new_employee.role = role
        return self.logic_wrapper.add_new_staff(new_employee)
