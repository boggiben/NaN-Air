from logic.logic_wrapper import LogicWrapper
from logic.staff_logic import Staff_Logic
from model.employee import Employee
from datetime import datetime


class Staff_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("\n")
        print(f'{"Starfsmenn":>45}')
        print("*" * 80)
        print("1. Allir starfsmenn")
        print("2. Allir flugmenn")
        print("3. Allir flugþjónar")
        print("4. Skrá starfsmann")
        print("5. Finna starfsmann (nota kt) ")
        print("6. Breyta starfsmannaupplýsingum (nema nafni og kt)")
        print("7. Lausir starfsmenn (á eftir að útfæra)")
        print("8. Uppteknir starfsmenn (á eftir að útfæra)")
        print("9. sjá vinnuferðir starfsmanns (nota kt) ")
        print("b. Fara í aðalvalmynd")
        print("*" * 80)

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
                        f"Kennitala: {elem.national_id:<10} | "
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
                        f"Kennitala: {elem.national_id:<10} | "
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
                        f"Kennitala: {elem.national_id:<10} | "
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
                    print( "\n")
                    print("1. Prenta vinnuyfirlit starfsmanns.")
                    print("b. Til baka.")
                    user_input = input()
                    if user_input == "1":
                        pass
                    elif user_input == "b":
                        break    
            elif user_input.lower() == "6":
                ssn = input("Skráðu kenntiölu starfsmanns til breytingar: ")

                # Tökum við bæði kennitölu án og með bandstriki
                if "-" not in ssn and len(ssn) == 10:
                    ssn = ssn[:6] + "-" + ssn[6:]

                employee = self.logic_wrapper.get_employee_by_ssn(ssn)
                if employee is None:
                    print("Enginn starfsmaður er með þessa kennitölu")
                else:
                    self.modify_staff_ui(employee)

            elif user_input.lower() == "7":
                voyage_date = input("Dagsetning: ")
                year, month, day = voyage_date.split("-")
                date = datetime(int(year), int(month), int(day))
                employees = self.logic_wrapper.see_unbooked_employees(date)

                if not employees:
                    print("Engir lausir starfsmenn.")
                else:
                    for employee in employees:
                        print(employee)

            elif user_input.lower() == "8":
                voyage_date = input("Dagsetning: ")
                year, month, day = voyage_date.split("-")
                date = datetime(int(year), int(month), int(day))
                employees = self.logic_wrapper.see_booked_employees(date)
                destination = self.logic_wrapper.see_booked_employees_departure(date)

                if not employees:
                    print("Engir bókaðir starfsmenn.")
                else:
                    for employee in employees:
                        print(f"{destination}: {employee}")

            elif user_input.lower() == "9":
                ssn = input("kennitala: ")

                if "-" in ssn:
                    ssn = ssn.replace("-", "")

                all_voyages = self.logic_wrapper.get_voayges_of_employee(ssn)
                for voyage in all_voyages:
                    print(voyage)

            elif user_input.lower() == "b":
                break
            else:
                print("Rangur innsláttur. Reyndu aftur.")

    def add_new_staff_ui(self):
        new_employee = Employee()
        name = input("Nafn: ")
        new_employee.name = name
        mobile_number = input("Símanúmer: ")
        new_employee.gsm = mobile_number
        email = input("Netfang: ")
        new_employee.email = email
        address = input("Heimilisfang: ")
        new_employee.address = address
        national_id = input("Kennitala: ")
        new_employee.national_id = national_id
        role = input("Staða: ")
        new_employee.role = role
        return self.logic_wrapper.add_new_staff(new_employee)

    def modify_staff_ui(self, employee):
        # Birtum núverandi upplýsingar og um biðjum svo um að fá nýjar upplýsingar frá notanda
        print(f"Núverandi upplýsingar: {employee}")

        new_address = (
            input("Nýtt heimilisfang (skildu eftir autt til að halda óbreyttu): ")
            or employee.address
        )
        new_mobile_number = (
            input("Nýtt símanúmer (skildu eftir autt til að halda óbreyttu): ")
            or employee.gsm
        )
        new_email = (
            input("Nýtt netfang (skildu eftir autt til að halda óbreyttu): ")
            or employee.email
        )
        new_role = (
            input("Ný staða (skildu eftir autt til að halda óbreyttu): ")
            or employee.role
        )

        employee.address = new_address
        employee.gsm = new_mobile_number
        employee.email = new_email
        employee.role = new_role

        if self.logic_wrapper.modify_staff(employee):
            print("Starfsmannaupplýsingar uppfærðar.")
        else:
            print("Uppfærsla á upplýsingum mistókst!")
