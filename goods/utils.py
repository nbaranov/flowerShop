import openpyxl

PATH_TO_FILE = '/home/nick/Documents/flowers.xlsx'

def read_excel(path_to_file, number_of_cols):
    work_book = openpyxl.load_workbook(path_to_file)
    sheet_names = work_book.sheetnames
    sheet = work_book[sheet_names[0]]

    data_table = []
    for row in range(2, sheet.max_row):
        data_row = [sheet.cell(row=row,column=col).value for col in range(1, number_of_cols+1)]
        if data_row[0] == None:
            continue
        else:    
            data_table.append(data_row)
    return data_table


if __name__ == '__main__':
    read_excel(PATH_TO_FILE, 4)