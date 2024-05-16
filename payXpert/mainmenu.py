from dao.employee_service import EmployeeService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from dao.financial_record_service import FinancialRecordService
from exception.exception import EmployeeNotFoundException, FinancialRecordException, PayrollGenerationException, TaxCalculationException
from entity.employee import Employee
from entity.payroll import Payroll
from entity.tax import Tax
from entity.financial_record import FinancialRecord


class MainMenu:
    @staticmethod
    def main_menu(cursor, conn):
        employee_service = EmployeeService(cursor, conn)
        payroll_service = PayrollService(cursor, conn)
        tax_service = TaxService(cursor, conn)
        financial_record_service = FinancialRecordService(cursor, conn)

        while True:
            print("Main Menu:")
            print("1. Employee Management")
            print("2. Payroll Management")
            print("3. Tax Management")
            print("4. Financial Record Management")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    MainMenu.employee_management(employee_service)
                except EmployeeNotFoundException as e:
                    print(e)
            elif choice == "2":
                try:
                    MainMenu.payroll_management(payroll_service)
                except PayrollGenerationException as e:
                    print(e)
            elif choice == "3":
                try:
                    MainMenu.tax_management(tax_service)
                except TaxCalculationException as e:
                    print(e)
            elif choice == "4":
                try:
                    MainMenu.financial_record_management(financial_record_service)
                except FinancialRecordException as e:
                    print(e)
            elif choice == "5":
                print("Goodbye! Come back soon")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def employee_management(employee_service):
        while True:
            print("Employee Management:")
            print("1. Create an employee")
            print("2. Delete an employee")
            print("3. Read employees")
            print("4. Update an employee")
            print("5. Exit to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_data = (
                    input("Enter first name: "),
                    input("Enter last name: "),
                    input("Enter date of birth (YYYY-MM-DD): "),
                    input("Enter gender: "),
                    input("Enter email: "),
                    input("Enter phone number: "),
                    input("Enter address: "),
                    input("Enter position: "),
                    input("Enter joining date (YYYY-MM-DD): "),
                    input("Enter termination date (YYYY-MM-DD, if any): "),
                )
                employee = Employee(*employee_data)
                employee_service.create_employee(employee)
            elif choice == "2":
                employee_service.read_employees()
                employee_id = input("Enter the EmployeeID: ")
                employee_service.delete_employee(employee_id)
            elif choice == "3":
                employee_service.read_employees()
            elif choice == "4":
                employee_service.read_employees()
                employee_data = (
                    input("Enter first name: "),
                    input("Enter last name: "),
                    input("Enter date of birth (YYYY-MM-DD): "),
                    input("Enter gender: "),
                    input("Enter email: "),
                    input("Enter phone number: "),
                    input("Enter address: "),
                    input("Enter position: "),
                    input("Enter joining date (YYYY-MM-DD): "),
                    input("Enter termination date (YYYY-MM-DD, if any): "),
                    input("Enter the EmployeeID to update: "),
                )
                employee_service.update_employee(employee_data)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def payroll_management(payroll_service):
        while True:
            print("Payroll Management:")
            print("1. Generate payroll for an employee")
            print("2. Get payroll by ID")
            print("3. Get payrolls for an employee")
            print("4. Get payrolls for a period")
            print("5. Exit to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter EmployeeID: ")
                start_date = input("Enter Pay Period Start Date (YYYY-MM-DD): ")
                end_date = input("Enter Pay Period End Date (YYYY-MM-DD): ")
                payroll_data = {
                    "employee_id": employee_id,
                    "start_date": start_date,
                    "end_date": end_date
                }
                payroll = Payroll(**payroll_data)
                payroll_service.generate_payroll(payroll)
            elif choice == "2":
                payroll_id = input("Enter PayrollID: ")
                payroll_service.get_payroll_by_id(payroll_id)
            elif choice == "3":
                employee_id = input("Enter EmployeeID: ")
                payroll_service.get_payrolls_for_employee(employee_id)
            elif choice == "4":
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                payroll_service.get_payrolls_for_period(start_date, end_date)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def tax_management(tax_service):
        while True:
            print("Tax Management:")
            print("1. Calculate tax for an employee")
            print("2. Get tax by ID")
            print("3. Get taxes for an employee")
            print("4. Get taxes for a year")
            print("5. Exit to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter EmployeeID: ")
                tax_year = input("Enter Tax Year: ")
                tax_data = {
                    "employee_id": employee_id,
                    "tax_year": tax_year
                }
                tax = Tax(**tax_data)
                tax_service.calculate_tax(tax)
            elif choice == "2":
                tax_id = input("Enter TaxID: ")
                tax_service.get_tax_by_id(tax_id)
            elif choice == "3":
                employee_id = input("Enter EmployeeID: ")
                tax_service.get_taxes_for_employee(employee_id)
            elif choice == "4":
                tax_year = input("Enter Tax Year: ")
                tax_service.get_taxes_for_year(tax_year)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def financial_record_management(financial_record_service):
        while True:
            print("Financial Record Management:")
            print("1. Add a financial record for an employee")
            print("2. Get financial record by ID")
            print("3. Get financial records for an employee")
            print("4. Get financial records for a date")
            print("5. Exit to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter EmployeeID: ")
                description = input("Enter description: ")
                amount = input("Enter amount: ")
                record_type = input("Enter record type: ")
                financial_record_data = {
                    "employee_id": employee_id,
                    "description": description,
                    "amount": amount,
                    "record_type": record_type
                }
                financial_record = FinancialRecord(**financial_record_data)
                financial_record_service.add_financial_record(financial_record)
            elif choice == "2":
                record_id = input("Enter RecordID: ")
                financial_record_service.get_financial_record_by_id(record_id)
            elif choice == "3":
                employee_id = input("Enter EmployeeID: ")
                financial_record_service.get_financial_records_for_employee(employee_id)
            elif choice == "4":
                record_date = input("Enter Record Date (YYYY-MM-DD): ")
                financial_record_service.get_financial_records_for_date(record_date)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
