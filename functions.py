def merging_sort(data):
    if len(data) == 1:
        return data
    mid = len(data)//2
    left = data[0:mid]
    right = data[mid:]
    merging_sort(left)
    merging_sort(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            data[k] = left[i]
            i+=1
            k+=1
        else:
            data[k] = right[j]
            j+=1
            k+=1
    while i < len(left):
        data[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        data[k] = right[j]
        j+=1
        k+=1

def binary_search(data,item):
    if len(data) == 0:  
        return "Item not found"
    mid = len(data) // 2
    left = data[0:mid]
    right = data[mid:]
    if data[mid][1] == item:
        return f"item you are looking for is: {data[mid]}"
    elif data[mid][1] > item:
        return binary_search(left,item)
    else:
        return binary_search(right,item)

