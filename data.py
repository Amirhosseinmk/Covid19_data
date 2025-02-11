import pandas as pd

excel_file = 'Covid.xlsx'
file = pd.read_excel(excel_file)
csv_file = 'data.csv'
file.to_csv(csv_file, index = False) #just extra thing to have csv version of excel file
csv = pd.read_csv(csv_file)
half = len(file)//2
first_half = file.loc[0:half]
list_first_half = first_half.values.tolist()
# for i in list_first_half:    #by debuging here we figure out data inserted from last to first , 
#     print(i)                  #we we insert item to doubly list , its first item is the last item from list_first_half 
second_half = file.loc[half+1:]
list_second_half = second_half.values.tolist()




