import datetime
import xlrd


# ----------------------------------------------------------------------
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    # print number of sheets
    print(book.nsheets)

    # print sheet names
    print(book.sheet_names())
    #
    # # get the first worksheet
    first_sheet = book.sheet_by_index(2)
    #
    # # read a row
    print(first_sheet.row_values(2))
    #
    # # read a cell
    cell = first_sheet.cell(6,2)
    print(cell)
    print(cell.value)
    #
    # # read a row slice
    print(xlrd.xldate_as_tuple(first_sheet.row_slice(rowx=5,
                          start_colx=1,
                          end_colx=6)[0].value,book.datemode))


# ----------------------------------------------------------------------
if __name__ == "__main__":
    path = r"D:\Data\Eneo\dev\fmms\media\imports\plan.xls"
    open_file(path)