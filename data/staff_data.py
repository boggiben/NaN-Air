import csv
from model.employee import Employee

# from model.staff import Staff


class Staff_Data:
    def __init__(self):
        self.file_name = "files/staff.csv"

    def create_staff(self, staff):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "name",
                "mobile_number",
                "email",
                "address",
                "national_id",
                "role",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "name": staff.name,
                    "national_id": staff.national_id,
                    "address": staff.address,
                    "mobile_number": staff.mobile_number,
                    "email": staff.email,
                    "role": staff.role,
                }
            )
            return True

    def read_all_staff(self):
        staff_list = []
        with open(
            self.file_name, mode="r", newline="", encoding="utf-8-sig"
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                staff_list.append(
                    Employee(
                        row["name"],
                        row["mobile_number"],
                        row["email"],
                        row["address"],
                        row["national_id"],
                        row["role"],
                    )
                )
        return staff_list

    def read_all_pilots(self):
        """Mjög svipað og read_all_staff nema að hérna filterum við flugmenn/flugstjóra"""
        pilots_list = []

        with open(
            self.file_name, mode="r", newline="", encoding="utf-8-sig"
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["role"] in ["Flugstjóri", "Flugmaður"]:
                    pilots_list.append(
                        Employee(
                            row["name"],
                            row["mobile_number"],
                            row["email"],
                            row["address"],
                            row["national_id"],
                            row["role"],
                        )
                    )
        return pilots_list

    def read_all_flight_attendants(self):
        """Mjög svipað og read_all_staff nema að hérna filterum við flugþjóna/yfirflugþjóna"""
        flight_attendants_list = []

        with open(
            self.file_name, mode="r", newline="", encoding="utf-8-sig"
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["role"] in ["Yfirflugþjónn", "Flugþjónn"]:
                    flight_attendants_list.append(
                        Employee(
                            row["name"],
                            row["mobile_number"],
                            row["email"],
                            row["address"],
                            row["national_id"],
                            row["role"],
                        )
                    )
        return flight_attendants_list

    def modify_staff(self, employee):
        employees = self.read_all_staff()
        updated = False
        for i, emp in enumerate(employees):
            if emp.national_id == employee.national_id:
                employees[i] = employee
                updated = True
                break

        if updated:
            self.write_all_staff(employees)
            return True
        else:
            return False

    def write_all_staff(self, employees):
        with open(self.file_name, "w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "name",
                "mobile_number",
                "email",
                "address",
                "national_id",
                "role",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp in employees:
                writer.writerow(
                    {
                        "name": emp.name,
                        "mobile_number": emp.gsm,
                        "email": emp.email,
                        "address": emp.address,
                        "national_id": emp.national_id,
                        "role": emp.role,
                    }
                )

    def see_available_employees(self):
        pass