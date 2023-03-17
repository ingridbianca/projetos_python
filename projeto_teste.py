import pandas as pd
import xlsxwriter

def create_file():
    workbook = xlsxwriter.Workbook('teste.xlsx')
    worksheet = workbook.add_worksheet()
    header_format = workbook.add_format({'bold': True, 'text_wrap': True, 'fg_color': '#6a75cc', 'border': 1})
    worksheet.write('A1', 'Hello!', header_format)
    
    workbook.close()


if __name__ == '__main__':
    create_file()
