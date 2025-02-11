from data import list_first_half ,list_second_half
from Doubly import Node,doubly_list
list_2D = doubly_list()

for info in list_first_half:
    list_2D.insert_head(info)

list_2D.display_forward()
