from datetime import datetime

class EmployeeService:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def read_employees(self):
        self.cursor.execute("SELECT * FROM Employee")
        employees = self.cursor.fetchall()
        for employee in employees:
            print(employee)

    def create_employee(self, employee_data):
        # Validate date formats
        try:
            for i in [2, 8, 9]:  # Indices of date fields in employee_data tuple
                if employee_data[i]:
                    datetime.strptime(employee_data[i], '%Y-%m-%d')  # Validate date format if not empty
        except ValueError:
            print("Invalid date format. Date should be in YYYY-MM-DD format.")
            return  # Stop execution if date format is invalid
        
        # Proceed with insertion
        self.cursor.execute(
            """
            INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            employee_data,  # No need to exclude EmployeeID
        )
        self.conn.commit()
        print("Employee inserted successfully.")

    def delete_employee(self, employee_id):
        self.cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,))
        self.conn.commit()
        print("Employee deleted successfully.")

    def update_employee(self, employee_data):
        # Validate date formats
        try:
            for i in [2, 8, 9]:  # Indices of date fields in employee_data tuple
                if employee_data[i]:
                    datetime.strptime(employee_data[i], '%Y-%m-%d')  # Validate date format if not empty
        except ValueError:
            print("Invalid date format. Date should be in YYYY-MM-DD format.")
            return  # Stop execution if date format is invalid
        
        # Proceed with update
        self.cursor.execute(
            """
            UPDATE Employee
            SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
            WHERE EmployeeID = ?
            """,
            employee_data,
        )
        self.conn.commit()
        print("Employee updated successfully.")

