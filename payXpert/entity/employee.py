class Employee:
    def __init__(self, employee_id, first_name, last_name, date_of_birth, gender, email, phone_number, address, position, joining_date, termination_date=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.position = position
        self.joining_date = joining_date
        self.termination_date = termination_date

