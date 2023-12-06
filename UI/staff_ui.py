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
            elif user_input.lower() == "q":
                break
            else:
                print("Rangur innsláttur. Reyndu aftur.")
