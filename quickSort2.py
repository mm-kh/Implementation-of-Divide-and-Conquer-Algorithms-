def quickSort(List,first,last):
    if first < last:
        q=partition(List,first,last)
        quickSort(List, first, q-1)
        quickSort(List, q+1, last)
    return List    


def partition(List,first,last):
    pivot=List[first]
    i=first+1
    j=last
    while i<=j:
        while List[i]<=pivot:
            i=i+1
        while List[j]>pivot:
            j=j-1
        if i<j:
            swap=List[j]
            List[j]=List[i]
            List[i]=swap
    swap=List[j]
    List[j]=List[first]
    List[first]=swap
    return j
    

List=[23,4,86,34,65,-22,12,17,13,7,89,76]
sortedList=quickSort(List,0,len(List)-1)
print(sortedList)