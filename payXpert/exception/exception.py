class EmployeeNotFoundException(Exception):
    """ raised when attempting to access or perform operations on a non-existing employee."""

    def __init__(self, message="Employee not found."):
        self.message = message
        super().__init__(self.message)

class PayrollGenerationException(Exception):
    """ raised when there is an issue with generating payroll for an employee. """

    def __init__(self, message="issue with generating payroll for an employee"):
        self.message = message
        super().__init__(self.message)

class TaxCalculationException(Exception):
    """  raised when there is an error in calculating taxes for an employee. """

    def __init__(self, message="error in calculating taxes for an employee."):
        self.message = message
        super().__init__(self.message)

class FinancialRecordException(Exception):
    """ raised when there is an issue with financial record management."""

    def  __init__(self, message="issue with financial record management"):
        self.message = message
        super().__init__(self.message)

class InvalidInputException(Exception):
    """ raised when input data doesn't meet the required criteria."""

    def  __init__(self, message="input data doesn't meet the required criteria,give correct one"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    """ raised  when there is a problem establishing or maintaining a connection with the database"""

    def  __init__(self, message="database connection problem"):
        self.message = message
        super().__init__(self.message)