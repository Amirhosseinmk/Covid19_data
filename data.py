import pandas as pd
import matplotlib.pyplot as plot

from functions import merging_sort
excel_file = 'Covid.xlsx'
file = pd.read_excel(excel_file)
csv_file = 'data.csv'
file.to_csv(csv_file, index = False) #just extra thing to have csv version of excel file
csv = pd.read_csv(csv_file)
half = len(file)//2


first_half = file.iloc[0:half+1][::-1]  
second_half = file.iloc[half+1:]

first10_country = file[['Total Cases','State/UTs']].head(10)
Country_info = list(zip(file['State/UTs'],file['Total Cases']))
merging_sort(Country_info)
plot.figure(figsize=(10,10))
plot.bar(first10_country["State/UTs"],first10_country["Total Cases"],color = 'blue')
plot.xlabel("State/UTs")
plot.ylabel("Total Cases")
plot.title("First 10 country Before Sorting")
plot.xticks(rotation = 90)
plot.show()

sorted_country = [i[0] for i in Country_info]
sorted_TotallCase = [i[1] for i in Country_info]
plot.bar(sorted_country[:10],sorted_TotallCase[:10], color='green')
plot.xlabel("State/UTs")
plot.ylabel("Total Cases")
plot.title("First 10 country after Sorting")
plot.xticks(rotation = 90)
plot.show()



# Convert to list
list_first_half = first_half.values.tolist()
list_second_half = second_half.values.tolist()
 


# print(list_second_half)
# print("---------------------------------------------------------")
# print(list_first_half)     just for debugging uncomment
for i in Country_info:
    print(i)


