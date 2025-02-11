import pandas as pd

excel_file = 'Covid.xlsx'
file = pd.read_excel(excel_file)
csv_file = 'data.csv'
file.to_csv(csv_file, index = False) #just extra thing to have csv version of excel file
csv = pd.read_csv(csv_file)
print(file) 