def QuickSort(List):
    if len(List)<=1:
        return List
    else:
        pivot=List.pop()
        smaller=[]
        greater=[]
        for i in List:
            if i<pivot:
                smaller.append(i)
            else:
                greater.append(i)


    List=QuickSort(smaller)+[pivot]+QuickSort(greater)
    return List

List=[53,23,45,9,50]
Resault=QuickSort(List)
print(Resault)