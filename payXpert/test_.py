import unittest
from unittest.mock import Mock, call
from dao.payroll_service import PayrollService
from dao.financial_record_service import FinancialRecordService
from dao.tax_service import TaxService
from dao.employee_service import EmployeeService
from datetime import datetime

class TestPayrollService(unittest.TestCase):
    def setUp(self):
        # Set up mock cursor and connection for payroll service
        self.mock_cursor_payroll = Mock()
        self.mock_conn_payroll = Mock()
        self.payroll_service = PayrollService(self.mock_cursor_payroll, self.mock_conn_payroll)

        # Set up mock cursor and connection for financial record service
        self.mock_cursor_financial = Mock()
        self.mock_conn_financial = Mock()
        self.financial_record_service = FinancialRecordService(self.mock_cursor_financial, self.mock_conn_financial)

    def test_calculate_gross_salary_for_employee(self):
        # Arrange
        basic_salary = 2000
        overtime_pay = 500
        
        # Act
        gross_salary = self.payroll_service.calculate_gross_salary_for_employee(basic_salary, overtime_pay)

        # Assert
        self.assertEqual(gross_salary, 2500)  # Expected gross salary: basic_salary + overtime_pay
    
    def test_calculate_net_salary_after_deductions(self):
        # Arrange
        basic_salary = 2000
        overtime_pay = 500
        deductions = 700  # Example deductions including taxes, insurance, etc.
        expected_net_salary = basic_salary + overtime_pay - deductions
        
        # Act
        net_salary = self.payroll_service.calculate_net_salary_after_deductions(basic_salary, overtime_pay, deductions)

        # Assert
        self.assertEqual(net_salary, expected_net_salary)


class TestTaxService(unittest.TestCase):
    def test_calculate_tax(self):
        # Arrange
        employee_id = 1
        tax_year = "2024"
        taxable_income = 50000  # Example taxable income
        expected_tax_amount = 0.2 * taxable_income  # Example: Assuming a flat 20% tax rate

        # Set up mock cursor object
        mock_cursor = Mock()
        mock_cursor.fetchone.return_value = (taxable_income,)

        # Set up mock connection object if needed
        mock_conn = Mock()

        # Create an instance of TaxService with the mock cursor and connection
        tax_service = TaxService(mock_cursor, mock_conn)

        # Act
        tax_service.calculate_tax(employee_id, tax_year)

        # Assert
        # Verify that execute method is called twice
        mock_cursor.execute.assert_has_calls([
            call('SELECT NetSalary FROM Payroll WHERE EmployeeID = ? AND PayPeriodStartDate <= ? AND PayPeriodEndDate >= ?', (1, '2024-01-01', '2024-12-31')),
            call('INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount) VALUES (?, ?, ?, ?)', (1, '2024', taxable_income, expected_tax_amount))
        ])
        mock_conn.commit.assert_called_once()

class TestEmployeeService(unittest.TestCase):
    def setUp(self):
        # Set up mock cursor and connection
        self.mock_cursor = Mock()
        self.mock_conn = Mock()

        # Initialize EmployeeService with mock cursor and connection
        self.employee_service = EmployeeService(self.mock_cursor, self.mock_conn)

class TestEmployeeService(unittest.TestCase):
    def setUp(self):
        # Set up mock cursor and connection
        self.mock_cursor = Mock()
        self.mock_conn = Mock()

        # Initialize EmployeeService with mock cursor and connection
        self.employee_service = EmployeeService(self.mock_cursor, self.mock_conn)

    def test_create_employee_with_invalid_date_format(self):
        # Test data with invalid date format (using 'invalid' instead of a valid date)
        invalid_employee_data = [
            "John", "Doe", "invalid", "M", "john.doe@example.com", "123456789", "123 Main St", "Manager", "2023-01-01", "2024-01-01"
        ]

        # Ensure that the method prints an error message and does not proceed with insertion
        with self.assertRaises(ValueError) as context:
            self.employee_service.create_employee(invalid_employee_data)

        # Assert that the error message was printed
        self.assertIn("Invalid date format", str(context.exception))

        # Ensure that the method did not execute SQL queries or commit
        self.mock_cursor.execute.assert_not_called()
        self.mock_conn.commit.assert_not_called()

if __name__ == '__main__':
    unittest.main()
