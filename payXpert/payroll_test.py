import unittest
from unittest.mock import Mock, MagicMock
from dao.payroll_service import PayrollService  # Adjust the import according to your project structure

class TestPayrollServiceModule(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = MagicMock()
        self.mock_conn = MagicMock()
        self.payroll_service = PayrollService(self.mock_cursor, self.mock_conn)

    def test_read_payrolls(self):
        self.mock_cursor.fetchall.return_value = [
            (1, 1, '2024-05-01', '2024-05-15', 2000, 10, 20, 500, 2500)
        ]
        payrolls = self.payroll_service.read_payrolls()
        self.mock_cursor.execute.assert_called_once_with("SELECT * FROM Payroll")
        self.assertIsNotNone(payrolls)
        self.assertEqual(len(payrolls), 1)
        self.assertEqual(payrolls[0], (1, 1, '2024-05-01', '2024-05-15', 2000, 10, 20, 500, 2500))

    def test_generate_payroll(self):
        employee_id = 1
        start_date = "2024-05-16"
        end_date = "2024-05-31"

        self.mock_cursor.fetchone.return_value = (1, 'John Doe')

        self.payroll_service.generate_payroll(employee_id, start_date, end_date)

        self.mock_cursor.execute.assert_any_call("SELECT * FROM Employee WHERE EmployeeID = ?", (employee_id,))
        self.mock_cursor.execute.assert_any_call(
            """
            INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimeHours, OvertimeRate, Deductions, NetSalary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (employee_id, start_date, end_date, 2000, 10, 20, 500, 2500)
        )
        self.mock_conn.commit.assert_called_once()

    def test_get_payroll_by_id(self):
        payroll_id = 1
        self.mock_cursor.fetchone.return_value = (1, 1, '2024-05-01', '2024-05-15', 2000, 10, 20, 500, 2500)

        payroll = self.payroll_service.get_payroll_by_id(payroll_id)
        self.mock_cursor.execute.assert_called_once_with("SELECT * FROM Payroll WHERE PayrollID = ?", (payroll_id,))
        self.assertIsNotNone(payroll)
        self.assertEqual(payroll, (1, 1, '2024-05-01', '2024-05-15', 2000, 10, 20, 500, 2500))

    def test_get_payrolls_for_employee(self):
        employee_id = 1
        self.mock_cursor.fetchall.return_value = [
            (1, 1, '2024-05-01', '2024-05-15', 2000, 10, 20, 500, 2500)
        ]

        payrolls = self.payroll_service.get_payrolls_for_employee(employee_id)
        self.mock_cursor.execute.assert_called_once_with("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
        self.assertIsNotNone(payrolls)
        self.assertEqual(len(payrolls), 1)
        self.assertEqual(payrolls[0][1], employee_id)

    def test_get_payrolls_for_period(self):
        start_date = "2024-05-01"
        end_date = "2024-05-15"
        self.mock_cursor.fetchall.return_value = [
            (1, 1, '2024-05-01', '2024-05-15', 2000, 10, 20, 500, 2500)
        ]

        payrolls = self.payroll_service.get_payrolls_for_period(start_date, end_date)
        self.mock_cursor.execute.assert_called_once_with(
            """
            SELECT * 
            FROM Payroll 
            WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?
            """, (start_date, end_date)
        )
        self.assertIsNotNone(payrolls)
        self.assertEqual(len(payrolls), 1)
        self.assertEqual(payrolls[0][2], start_date)
        self.assertEqual(payrolls[0][3], end_date)

if __name__ == "__main__":
    unittest.main()
