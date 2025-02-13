def bubble_sort(data):
    size = len(data)
    for _ in range(0,size):
        for i in range(0,size - 1):
            j = i + 1
            if data[i][1] > data[j][1]:
                data[i], data[j] = data[j],data[i]
   

def search(data,item):
    for i  in range(0,len(data)):
        if data[i] == item:
            return data[i]