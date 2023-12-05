from data.staff_data import Staff_Data

class DataWrapper:
    def __init__(self):
        self.staff_data = Staff_Data()
        
    def create_staff(self, employee):
        self.staff_data.create_staff(employee)
        
    def get_all_staff(self):