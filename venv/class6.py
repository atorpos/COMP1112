from math import log

import openpyxl

import json

filepath = "sampel_python.xlsx"
active_count = 0
workbook = openpyxl.load_workbook(filepath)
sheet = workbook.active
cell_obj = sheet.cell(row = 1, column = 1)
print(cell_obj.value)
# sheet.oo

for row in sheet.iter_rows():
    for cell in row:
        if cell.value is not None:
            print(cell.value)
            active_count +=1

print(f"number of cells: {active_count} ")

workbook.close()

def addno():
    sum = 5 + 4
    print(sum)


def mynaem():
    first_name = "same"
    last_name = "joh"
    print(last_name)


# global variable
c = 1


def addnum():
    global c
    # global vqriable
    c = c + 1
    print(c)

switch

addnum()
# addno()
print(c)
