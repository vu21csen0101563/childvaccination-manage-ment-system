from datetime import datetime, timedelta

class VaccinationManagementSystem:
    def __init__(self):
        self.child_records = {}
        self.appointments = {}

    def add_child_record(self, child_id, name, dob, parent_contact):
        self.child_records[child_id] = {
            "name": name,
            "dob": dob,
            "parent_contact": parent_contact
        }
        print(f"Child record added: {name}")

    def book_appointment(self, child_id, vaccine_name, appointment_date):
        if child_id not in self.child_records:
            print("Child record not found.")
            return

        if child_id not in self.appointments:
            self.appointments[child_id] = []

        self.appointments[child_id].append({
            "vaccine_name": vaccine_name,
            "appointment_date": appointment_date
        })
        print(f"Appointment booked for {self.child_records[child_id]['name']} on {appointment_date} for {vaccine_name}.")

    def send_reminders(self):
        today = datetime.now().date()
        for child_id, appointments in self.appointments.items():
            for appointment in appointments:
                appointment_date = appointment["appointment_date"]
                days_left = (appointment_date - today).days
                if 0 <= days_left <= 2:
                    child_name = self.child_records[child_id]['name']
                    parent_contact = self.child_records[child_id]['parent_contact']
                    print(f"Reminder: {child_name} has a vaccination appointment for {appointment['vaccine_name']} on {appointment_date}. Contact: {parent_contact}")

    def view_appointments(self, child_id):
        if child_id not in self.appointments:
            print("No appointments found for this child.")
            return

        print(f"Appointments for {self.child_records[child_id]['name']}:")
        for appointment in self.appointments[child_id]:
            print(f"- {appointment['vaccine_name']} on {appointment['appointment_date']}")


# Example usage
system = VaccinationManagementSystem()
system.add_child_record(1, "John Doe", "2019-05-01", "123-456-7890")
system.book_appointment(1, "MMR Vaccine", datetime(2024, 9, 1).date())
system.book_appointment(1, "Polio Vaccine", datetime(2024, 10, 15).date())

system.view_appointments(1)

system.send_reminders()
