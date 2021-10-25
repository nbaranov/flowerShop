from abc import ABC, abstractmethod

import openpyxl


class Parser(ABC):
    @abstractmethod
    def parse(self, file):
        raise NotImplementedError()


class ExcelParser(Parser):
    def parse(self, file):
        # TODO обработка ошибок, учесть external_id
        work_book = openpyxl.load_workbook(file)
        sheet_names = work_book.sheetnames
        sheet = work_book[sheet_names[0]]

        data_table = []
        for row in range(2, sheet.max_row):
            data_row = [sheet.cell(row=row, column=col).value for col in range(1, sheet.max_col+1)]
            if data_row[0] is None:
                continue
            else:
                data_table.append(data_row)
        return data_table


class CsvParser(Parser):
    def parse(self, file):
        # TODO сам догадайся )
        pass