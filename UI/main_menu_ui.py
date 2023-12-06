from logic.logic_wrapper import LogicWrapper
from ui.staff_ui import Staff_UI
from ui.destination_ui import Destination_UI


class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        print("\n")
        print(f"{'Velkomin/n á aðalvalmynd':^75}")
        print("*" * 80)

        print(f"{'1. Starfsmenn':<80}")
        print(f"{'2. Áfangastaðir':<80}")
        print(f"{'3. Flugferðir':<80}")
        print(f"{'4. Vinnuferðir':<80}")
        print(f"{'5. Skrá starfsmann í vinnuferð':<80}")
        print(f"{'6. Skrá nýjan starfsmann':<80}")
        print(f"{'q. Hætta':<80}")
        print("*" * 80)
        print(ascii)
        print("*" * 80)

    def input_main_menu(self):
        while True:
            self.menu_output()
            user_input = input("Veldu aðgerð: ")
            user_input = user_input.lower()
            if user_input == "1":
                menu = Staff_UI(self.logic_wrapper)
                menu.input_staff_menu()
                # self.logic_wrapper.get_all_staff()
            elif user_input == "2":
                menu = Destination_UI(self.logic_wrapper)
                menu.input_destination()
            elif user_input == "3":
                self.logic_wrapper.get_all_flights()
            elif user_input == "4":
                self.logic_wrapper.add_new_flight()
            elif user_input == "5":
                self.logic_wrapper.add_staff_to_flight()
            elif user_input == "6":
                self.logic_wrapper.add_new_staff()
            elif user_input == "7":
                self.logic_wrapper.get_flights_by_week()
            elif user_input == "q":
                print("Bless")
                break
            else:
                print("Rangur innsláttur")


ascii = """                          
            __/\__                              
           `==/\==`
 ____________/__\____________
/____________________________/
  __||__||__/.--.\__||__||__
 /__|___|___( >< )___|___|__/
           _/`--`\_
          (/------\)
               """
