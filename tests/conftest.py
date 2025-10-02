import openpyxl
import pytest

def read_excel_data(filePath, sheetName):
    workBook =openpyxl.load_workbook(filePath)
    sheet = workBook[sheetName]
    data = []

    for row in sheet.iter_rows(min_row=2,values_only=True):
        username = str(row[0].strip())
        password = str(row[1].strip())
        data.append((username, password))
    return  data

def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames and "password"  in metafunc.fixturenames:
        data = read_excel_data("testData.xlsx", "Sheet1")
        metafunc.parametrize(("username", "password"), data)

