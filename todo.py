from data import list_first_half ,list_second_half ,Country_info
from Doubly import Node,doubly_list
from functions import binary_search
list_2D = doubly_list()
for i in list_first_half:  
    list_2D.insert_head(i)  # Ensures first half remains in order
print("------------------------------------------------------------")


for j in list_second_half:
    list_2D.insert_tail(j)  





list_2D.display_forward()
print("------------------------------------------------------------")
list_2D.display_backward()





print(binary_search(Country_info,55216))