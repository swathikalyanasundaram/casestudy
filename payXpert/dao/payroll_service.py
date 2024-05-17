import pyodbc
from datetime import datetime

class PayrollService:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def process_payroll_for_multiple_employees(self, employees_data):
        for employee_data in employees_data:
            employee_id = employee_data["id"]
            basic_salary = employee_data["basic_salary"]
            overtime_pay = employee_data["overtime_pay"]
            deductions = employee_data["deductions"]

            net_salary = self.calculate_net_salary_after_deductions(basic_salary, overtime_pay, deductions)

            self.cursor.execute(
                """
                INSERT INTO PayrollRecords (EmployeeID, BasicSalary, OvertimePay, Deductions, NetSalary)
                VALUES (?, ?, ?, ?, ?)
                """,
                (employee_id, basic_salary, overtime_pay, deductions, net_salary)
            )
            self.conn.commit()

    def calculate_gross_salary_for_employee(self, basic_salary, overtime_pay):
        return basic_salary + overtime_pay
    
    def calculate_net_salary_after_deductions(self, basic_salary, overtime_pay, deductions):
        return basic_salary + overtime_pay - deductions

    def read_payrolls(self):
        self.cursor.execute("SELECT * FROM Payroll")
        payrolls = self.cursor.fetchall()
        return payrolls

    def generate_payroll(self, employee_id, start_date, end_date):
        self.cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?", (employee_id,))
        employee = self.cursor.fetchone()

        basic_salary = 2000   
        overtime_hours = 10  
        overtime_rate = 20  
        deductions = 500  

        net_salary = basic_salary + (overtime_hours * overtime_rate) - deductions

        self.cursor.execute(
            """
            INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimeHours, OvertimeRate, Deductions, NetSalary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (employee_id, start_date, end_date, basic_salary, overtime_hours, overtime_rate, deductions, net_salary),
        )
        self.conn.commit()
        print("Payroll generated successfully.")

    def get_payroll_by_id(self, payroll_id):
        self.cursor.execute("SELECT * FROM Payroll WHERE PayrollID = ?", (payroll_id,))
        payroll = self.cursor.fetchone()
        return payroll

    def get_payrolls_for_employee(self, employee_id):
        self.cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
        payrolls = self.cursor.fetchall()
        return payrolls

    def get_payrolls_for_period(self, start_date, end_date):
        self.cursor.execute(
            """
            SELECT * 
            FROM Payroll 
            WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?
            """, (start_date, end_date)
        )
        payrolls = self.cursor.fetchall()
        return payrolls
