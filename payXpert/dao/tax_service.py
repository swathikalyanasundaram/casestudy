import pyodbc

class TaxService:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def read_taxes(self):
        self.cursor.execute("SELECT * FROM Tax")
        taxes = self.cursor.fetchall()
        for tax in taxes:
            print(f"TaxID: {tax[0]}, EmployeeID: {tax[1]}, TaxYear: {tax[2]}, TaxableIncome: {tax[3]}, TaxAmount: {tax[4]}")

    def calculate_tax(self, employee_id, tax_year):
        # Fetch the taxable income from the Payroll table
        self.cursor.execute("SELECT NetSalary FROM Payroll WHERE EmployeeID = ? AND PayPeriodStartDate <= ? AND PayPeriodEndDate >= ?",
                            (employee_id, tax_year + "-01-01", tax_year + "-12-31"))
        result = self.cursor.fetchone()
        if result:
            taxable_income = float(result[0])
        else:
            print("No payroll record found for the specified employee and tax year.")
            return

        # Perform tax calculation based on taxable income and tax year
        tax_amount = 0.2 * taxable_income  # Example: Assuming a flat 20% tax rate

        # Insert the calculated tax amount into the Tax table
        self.cursor.execute("INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount) VALUES (?, ?, ?, ?)",
                            (employee_id, tax_year, taxable_income, tax_amount))
        self.conn.commit()
        print("Tax calculated and recorded successfully.")

    def get_tax_by_id(self, tax_id):
        self.cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", (tax_id,))
        tax = self.cursor.fetchone()
        if tax:
            print(f"TaxID: {tax[0]}, EmployeeID: {tax[1]}, TaxYear: {tax[2]}, TaxableIncome: {tax[3]}, TaxAmount: {tax[4]}")
        else:
            print("No tax record found for the specified TaxID.")

    def get_taxes_for_employee(self, employee_id):
        self.cursor.execute("SELECT * FROM Tax WHERE EmployeeID = ?", (employee_id,))
        taxes = self.cursor.fetchall()
        for tax in taxes:
            print(f"TaxID: {tax[0]}, EmployeeID: {tax[1]}, TaxYear: {tax[2]}, TaxableIncome: {tax[3]}, TaxAmount: {tax[4]}")

    def get_taxes_for_year(self, tax_year):
        self.cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", (tax_year,))
        taxes = self.cursor.fetchall()
        if taxes:
            for tax in taxes:
                print(f"TaxID: {tax[0]}, EmployeeID: {tax[1]}, TaxYear: {tax[2]}, TaxableIncome: {tax[3]}, TaxAmount: {tax[4]}")
        else:
            print("No tax records found for the specified tax year.")

