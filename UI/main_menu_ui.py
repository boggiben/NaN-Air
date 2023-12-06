from logic.logic_wrapper import LogicWrapper
from ui.staff_ui import Staff_UI


class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        print("Velkominn á aðalvalmynd")
        print("1. Skoða öll skráð flug")
        print("2. Skoða flug vikunnar")
        print("3. Listi yfir starfsmenn")
        print("4. Skrá nýja flugferð")
        print("5. Skrá starfsmann í vinnuferð")
        print("6. Skrá nýjan starfsmann")
        print("q. Hætta")
        print("*" * 30)
        print(
            """                          
            __/\__
           `==/\==`
 ____________/__\____________
/____________________________/
  __||__||__/.--.\__||__||__
 /__|___|___( >< )___|___|__/
           _/`--`\_
          (/------\)
               """
        )
        print("*" * 30)

    def input_main_menu(self):
        while True:
            self.menu_output()
            user_input = input("Veldu aðgerð: ")
            user_input = user_input.lower()
            if user_input == "1":
                self.logic_wrapper.get_all_flights()
            elif user_input == "2":
                self.logic_wrapper.get_flights_by_week()
            elif user_input == "3":
                menu = Staff_UI(self.logic_wrapper)
                menu.input_staff_menu()
                # self.logic_wrapper.get_all_staff()
            elif user_input == "4":
                self.logic_wrapper.add_new_flight()
            elif user_input == "5":
                self.logic_wrapper.add_staff_to_flight()
            elif user_input == "6":
                self.logic_wrapper.add_new_staff()
            elif user_input == "q":
                print("Bless")
                break
            else:
                print("Rangur innsláttur")
