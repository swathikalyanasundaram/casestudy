import pyodbc
from dao.employee_service import EmployeeService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from dao.financial_record_service import FinancialRecordService
from mainmenu import MainMenu

print(f"welcome the the payxpert(payroll management)")

server_name = "MSI\\SQLEXPRESS"
database_name = "payxpert"

conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

if __name__ == "__main__":
    MainMenu.main_menu(cursor, conn)
