from data.data_wrapper import DataWrapper
from model.voyage import Voyage
from datetime import datetime, timedelta
import csv

# file_name = "files/past_flights.csv"
# file_name2 = "files/staff.csv"


class Voyage_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def create_voyage(self, voyage):
        """Takes in a voyage object and forwards it to the data layer"""

        self.data_wrapper.create_voyage(voyage)

    def get_all_voyages(self):
        return self.data_wrapper.get_all_voyages()

    def list_all_voyages(self):
        """This function lists all voyages in a neat format. One voyage is a roundtrip, with at least one captain,
        one copilot and one flight service manager"""

        all_voyages = self.get_all_voyages()  # Retrieve all voyages
        voyages_list = []
        paired_voyages = set()

        for i, voyage1 in enumerate(all_voyages):
            if i in paired_voyages:
                continue

            departure_date1 = datetime.strptime(
                voyage1.departure_time, "%Y-%m-%d %H:%M:%S"
            ).date()  # Extract date from voyage1 departure_time

            for j, voyage2 in enumerate(all_voyages):
                if j in paired_voyages or i == j:
                    continue

                departure_date2 = datetime.strptime(
                    voyage2.departure_time, "%Y-%m-%d %H:%M:%S"
                ).date()  # Extract date from voyage2 departure_time

                # Check for inverse route and same date
                if (
                    voyage1.departure == voyage2.arrival
                    and voyage1.arrival == voyage2.departure
                    and departure_date1 == departure_date2
                ):
                    voyages_list.append((voyage1, voyage2))
                    paired_voyages.update([i, j])
                    break

        return voyages_list

    def add_new_voyage(self, voyage):
        return self.data_wrapper.create_voyage(voyage)

    def get_voyage_by_date(self, voyage_date):
        all_voyages = self.get_all_voyages()
        voyages_for_date = []
        voyages_by_date = set()

        for i, voyage1 in enumerate(all_voyages):
            date1, _ = voyage1.departure_time.split()
            year1, month1, day1 = date1.split("-")
            date1 = datetime(int(year1), int(month1), int(day1))

            if date1 != voyage_date or i in voyages_by_date:
                continue

            for j, voyage2 in enumerate(all_voyages):
                if j in voyages_by_date or i == j:
                    continue

                date2, _ = voyage2.departure_time.split()
                year2, month2, day2 = date2.split("-")
                date2 = datetime(int(year2), int(month2), int(day2))

                if date2 != voyage_date:
                    continue

                if (
                    voyage1.departure == voyage2.arrival
                    and voyage1.arrival == voyage2.departure
                    and date1 == date2
                ):
                    voyages_for_date.append((voyage1, voyage2))
                    voyages_by_date.update([i, j])

        return voyages_for_date

    def get_voyage_by_week(self, start_date):
        end_date = start_date + timedelta(days=7)
        paired_voyages = set()
        grouped_voyages_weekly = []

        current_date = start_date
        while current_date <= end_date:
            daily_voyage_pairs = self.get_voyage_by_date(
                current_date
            )  # Returns pairs of voyages

            for pair in daily_voyage_pairs:
                for i, voyage1 in enumerate(pair):
                    # Check if voyage1 is already paired
                    if any(voyage1 in voyages for voyages in grouped_voyages_weekly):
                        continue

                    for j, voyage2 in enumerate(pair):
                        if voyage1 == voyage2:
                            continue

                        if (
                            voyage1.departure == voyage2.arrival
                            and voyage1.arrival == voyage2.departure
                        ):
                            grouped_voyages_weekly.append((voyage1, voyage2))
                            paired_voyages.update([voyage1, voyage2])
                            break

            current_date += timedelta(days=1)

        return grouped_voyages_weekly

    def see_booked_employees(self, voyage_date):
        all_voyages = self.get_all_voyages()
        employee_list = []
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')

        for voy in all_voyages:
            dep_time = datetime.strptime(voy.departure_time, "%Y-%m-%d %H:%M:%S")
            arr_time = datetime.strptime(voy.arrival_time, "%Y-%m-%d %H:%M:%S")
            try:
                if (
                    voyage_date.date() == dep_time.date()
                    or voyage_date.date() == arr_time.date()
                ):
                    employee_list.append(voy.captain)
                    employee_list.append(voy.copilot)
                    employee_list.append(voy.fsm)
                    #
                    if voy.fa1 != "":
                        employee_list.append(voy.fa1)
                    if voy.fa2 != "":
                        employee_list.append(voy.fa2)
            except:
                ValueError
                return "ValueError"
        unique_list = list(set(employee_list))

        return unique_list

    def see_unbooked_employees(self, voyage_date):
        all_voyages = self.get_all_voyages()
        employee_list = []
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')
        for voy in all_voyages:
            dep_time = datetime.strptime(voy.departure_time, "%Y-%m-%d %H:%M:%S")
            arr_time = datetime.strptime(voy.arrival_time, "%Y-%m-%d %H:%M:%S")
            if (
                voyage_date.date() != dep_time.date()
                or voyage_date.date() != arr_time.date()
            ):
                employee_list.append(voy.captain)
                employee_list.append(voy.copilot)
                employee_list.append(voy.fsm)

                if voy.fa1 != "":
                    employee_list.append(voy.fa1)
                if voy.fa2 != "":
                    employee_list.append(voy.fa2)
        unique_list = list(set(employee_list))

        return unique_list

    def see_booked_employees_departure(self, voyage_date):
        all_voyages = self.get_all_voyages()
        arrival = ""
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')

        for voy in all_voyages:
            dep_time = datetime.strptime(voy.departure_time, "%Y-%m-%d %H:%M:%S")
            arr_time = datetime.strptime(voy.arrival_time, "%Y-%m-%d %H:%M:%S")
            if (
                voyage_date.date() == dep_time.date()
                or voyage_date.date() == arr_time.date()
            ):
                arrival = str(voy.arrival)

            return arrival

    def get_voayges_of_employee(self, ssn, start_date_input):
        all_voyages = self.list_all_voyages()
        voyages_that_employee_works_in = []
        try:
            # Convert user input start date to datetime object
            user_start_date = datetime.strptime(start_date_input, "%Y-%m-%d")

            # Convert user_start_date to datetime with time of midnight
            user_start_datetime = datetime.combine(user_start_date, datetime.min.time())

            # Calculate the end of the week (7 days later)
            user_end_date = user_start_date + timedelta(days=7)

            for voyages_tuple in all_voyages:
                for voyage in voyages_tuple:
                    # Extract date from voyage departure_time
                    departure_date = datetime.strptime(
                        voyage.departure_time, "%Y-%m-%d %H:%M:%S"
                    ).date()

                    # Convert departure_date to datetime with time of midnight
                    departure_datetime = datetime.combine(
                        departure_date, datetime.min.time()
                    )

                    if (
                        voyage.captain == ssn
                        or voyage.copilot == ssn
                        or voyage.fsm == ssn
                        or voyage.fa1 == ssn
                        or voyage.fa2 == ssn
                    ) and user_start_datetime <= departure_datetime < user_start_datetime + timedelta(
                        days=7
                    ):
                        voyages_that_employee_works_in.append(voyage)
        except ValueError:
            return None
        return voyages_that_employee_works_in

    def see_voyage_plan(self, ssn):
        pass

    def see_booked_employees_name(self, employee):
        all_staff = self.data_wrapper.get_all_staff()
        name = ""
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')

        for staff in all_staff:
            if employee == staff.national_id:
                name = str(staff.name)

        return name

    def see_booked_employees_phone(self, employee):
        all_staff = self.data_wrapper.get_all_staff()
        phone = ""
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')
        for staff in all_staff:
            if employee == staff.national_id:
                phone = str(staff.gsm)

        return phone

    # def add_staff_to_voyage(self,flight_number,flight_number2,captain,copilot,flight_service_manager,flight_attendant_one="ENGINN",flight_attendant_two="ENGINN"):
    #     all_voyages = self.get_all_voyages()
    #     for voy in all_voyages:
    #         if flight_number == voy.flight_number:
    #             voy.captain=captain
    #             voy.copilot=copilot
    #             voy.flight_service_manager=flight_service_manager
    #             voy.flight_attendant_one=flight_attendant_one
    #             voy.flight_attendant_two=flight_attendant_two
    #     flight_number2=0
                
                
    def check_flight_number(self, flight_number):
        all_voyages = self.get_all_voyages()
        for voyage in all_voyages:
            if flight_number == voyage.flight_number:
                return voyage
        return False
    
    # def modify_voyage(self, voyage):
    #     voyages = self.get_all_voyages()
    #     updated = False
    #     for i, voy in enumerate(voyages):
    #         if voy.flight_number == voyage.flight_number:
    #             voyages[i] = voyage
    #             updated = True
    #             break

    #     if updated:
    #         return self.data_wrapper.add_staff_to_flight(voyages)
    #     else:
    #         return False

    def modify_voyage(self, voyage):
        # Update the voyage
        return self.data_wrapper.update_voyage(voyage)

    def update_voyage(self, updated_voyage):
        voyages = self.data_wrapper.get_all_voyages()
        for i, voyage in enumerate(voyages):
            if voyage.flight_number == updated_voyage.flight_number:
                voyages[i] = updated_voyage
                self.data_wrapper.voyage_data.write_all_voyages(voyages)
                return True
        return False

    def combine_flights_voyage(self, voyage1_flight_number, voyage2_flight_number, new_captain, new_copilot, new_flight_service_manager, new_fa1, new_fa2, new_staffed):
        """This function takes in parameters from voyage_ui via the logic_wrapper, puts updated_voyages into a list so we can update the flight crew for both legs
        of the flight, which is one work trip"""
        voyage1 = self.check_flight_number(voyage1_flight_number)
        voyage2 = self.check_flight_number(voyage2_flight_number)

        if not voyage1 or not voyage2:
            return False

        updated_voyages = []
        for voyage in [voyage1, voyage2]:
            voyage.captain = new_captain
            voyage.copilot = new_copilot
            voyage.fsm = new_flight_service_manager
            voyage.fa1 = new_fa1
            voyage.fa2 = new_fa2
            voyage.staffed = new_staffed
            updated_voyages.append(voyage)

        return all(self.update_voyage(voyage) for voyage in updated_voyages)
    
    def duplicate_voyage(self, voyage, new_date):
        all_voyages = self.get_all_voyages()
        for voy in all_voyages:
            if voyage == voy.flight_number:
                flight_number=voy.flight_number
                