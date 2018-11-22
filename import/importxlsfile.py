import datetime
import os, re
import openpyxl
import itertools
import collections

fpath = r"D:\Data\Eneo\dev\fmms\media\imports"
class WorkBook(object):

    def __init__(self,filepath, filename):
        self.FILEPATH = filepath
        self.FILENAME = filename
        self.OPENWORKBOOK = self.readFile()
        # self.SHEET = self.getsheets()
        # self.ordeddictionary = collections.OrderedDict
        self.NULLCELLVALUES = lambda row:map(lambda cell:cell.value,row) # maps a list of rows of list of cells in that row, in order to extract its values
        self.NONNULLCELLVALUES = lambda cell_values: itertools.filterfalse(lambda cell_value: cell_value is None, cell_values)

    def readFile(self):
        return openpyxl.load_workbook(os.path.join(self.FILEPATH, self.FILENAME), data_only=True)

    def makeZip(self):
        opened_sheet = self.getSheetByName('Suivi Conso HFO')
        return opened_sheet.iter_cols(max_row=2, max_col=9)

    def getSheetsNames(self):
        return self.OPENWORKBOOK.get_sheet_names()

    # def sheetNametodate(self):
    #     self.listofdates = []
    #     for i in range(len(self.sheetsname)):
    #         try:
    #             cleanv = self.sheetsname[i].replace('-','').split()[0]
    #             if not(re.match(r'\d+',cleanv)): #filtring the digits from text
    #                 print('none')
    #                 continue
    #             else:
    #                 dd = cleanv[:2]
    #                 mm = cleanv[2:4]
    #                 yyyy = cleanv[4:]
    #                 if len(yyyy)<4:
    #                     yyyy='2018'
    #                 print(([dd,mm,yyyy,cleanv]))
    #                 self.listofdates.append(datetime.date(int(yyyy),int(mm),int(dd)))
    #         except ValueError:
    #             continue
    #     return self.listofdates
        # print('count is {} and sheet is {}'.format(str(n),str(len(self.sheetsname))))

    # def rdsheetvalues(self,sheetname):
    #     readsheet =self.workbk.get_sheet_by_name(sheetname)
    #     # print([readsheet['H1'].value,readsheet['H4'].value,readsheet['J1'].value,readsheet['K1'].value])
    #     v=lambda s:list(map(lambda x:x.value,s)) # using map to iterate over a list of list
    #     for i,r in enumerate(readsheet.rows):
    #         print([i,v(r)])

    def getSheetByName(self,sheetname):
        return self.OPENWORKBOOK.get_sheet_by_name(sheetname)

    def openCollectFile(self,opened_sheet):
        # allrows = rdsheet.rows
        # p_plants=set(self.lambdax(allrows[:1]))
        # type_fuel=set(self.lambdax(list(allrows)[0]))
        for index, row in enumerate(opened_sheet.iter_rows):
            if index == 0:
                all_power_plant_names = list(self.NONNULLCELLVALUES(self.NULLCELLVALUES(row)))
            elif index==1:
                fuel_type_list =list( self.NULLCELLVALUES(row))[:10]
            elif index==2:
                titles = list(self.NULLCELLVALUES(row))
                break
        return titles[1:10], all_power_plant_names
        # for i,r in enumerate(rdsheet.rows):
        #     # if i==
        #     print([i,r])

    def avalablePowerSheet(self, opened_powersheet):
        # data = opened_powersheet[:4]
        date = opened_powersheet['A1'].value
        centrale = opened_powersheet['A3'].value
        # max_col = len(list(data))
        # s = list(self.NULLCELLVALUES(data))
        return date.ctime(),centrale.ctime()#,centrale, [list(self.NULLCELLVALUES(u)) for u in opened_powersheet.iter_rows(min_row=3, max_row=26)]






        # d = datetime.date(*[int(i) for i in self.sheetsname[0].split('-')[::-1]])
b = WorkBook(fpath,'power.xlsx')
# for sheet in b.sheetsname:
#     if not(re.match(r'\d+',sheet.split()[0])):
#         continue
#
#     print(b.rdsheetvalues(sheet))
#     try:
#
# #         # cleanv = self.sheetsname[i].replace('-', '').split()[0]
#         if not (re.match(r'\d+',re.sub(r'\D',sheet.split()[0]))):  # filtring the digits from text
#             print(sheet)
#             continue
# #
#         print(b.rdsheetvalues(sheet))
#     except:
#         continue
# print(b.rdsheetvalues('Suivi Conso HFO'))
# print(b.openCollectFile())
# print(list(b.makeZip()))
print(b.avalablePowerSheet(b.getSheetByName('Limbe')))