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
        
        try:
            for i in [2, 8, 9]:  
                if employee_data[i]:
                    datetime.strptime(employee_data[i], '%Y-%m-%d')  
        except ValueError:
            print("Invalid date format. Date should be in YYYY-MM-DD format.")
            return  
        
        
        self.cursor.execute(
            """
            INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            employee_data, 
        )
        self.conn.commit()
        print("Employee inserted successfully.")

    def delete_employee(self, employee_id):
        self.cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,))
        self.conn.commit()
        print("Employee deleted successfully.")

    def update_employee(self, employee_data):
        
        try:
            for i in [2, 8, 9]: 
                if employee_data[i]:
                    datetime.strptime(employee_data[i], '%Y-%m-%d') 
        except ValueError:
            print("Invalid date format. Date should be in YYYY-MM-DD format.")
            return 
        
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

