import pyodbc
from datetime import datetime

class FinancialRecordService:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def read_financial_records(self):
        self.cursor.execute("SELECT * FROM FinancialRecord")
        records = self.cursor.fetchall()
        for record in records:
            print(record)

    def add_financial_record(self, employee_id, description, amount, record_type):
        self.cursor.execute(
            "INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType) VALUES (?,?,?,?,?)",
            (employee_id, datetime.now(), description, amount, record_type),
        )
        self.conn.commit()
        print("Financial record added successfully.")

    def get_financial_record_by_id(self, record_id):
        self.cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID = ?", (record_id,))
        record = self.cursor.fetchone()
        print(record)

    def get_financial_records_for_employee(self, employee_id):
        self.cursor.execute(
            "SELECT * FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,)
        )
        records = self.cursor.fetchall()
        for record in records:
            print(record)

    def get_financial_records_for_date(self, record_date):
        self.cursor.execute(
            "SELECT * FROM FinancialRecord WHERE RecordDate = ?", (record_date,)
        )
        records = self.cursor.fetchall()
        for record in records:
            print(record)
