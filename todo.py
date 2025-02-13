from data import list_first_half ,list_second_half
from Doubly import Node,doubly_list
list_2D = doubly_list()
for i in list_first_half:  
    list_2D.insert_head(i)  # Ensures first half remains in order
print("------------------------------------------------------------")


for j in list_second_half:
    list_2D.insert_tail(j)  





list_2D.display_forward()
print("------------------------------------------------------------")
list_2D.display_backward()
