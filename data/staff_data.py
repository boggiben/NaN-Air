import csv
# from model.staff import Staff


class Staff_Data:
    def __init__(self):
        #print(os.getcwd())
        self.file_name= = "files/staff.csv"

    def create_staff(self, staff):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "national_id", "address", "mobile_number", "email", "role"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': staff.name, 'national_id': staff.national_id, 'address': staff.address,
            'mobile_number': staff.mobile_number, 'email': staff.email, 'role': staff.role
            })



    # def read_all_customers(self):
    #     ret_list = []
    #     with open(self.file_name, newline='', encoding="utf-8") as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             ret_list.append(Customer(row["name"], row["birth_year"]))
    #     return ret_list

