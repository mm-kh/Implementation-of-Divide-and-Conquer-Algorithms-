def MergeSort(List):
    if len(List)>1:
        mid = len(List)//2
        LeftList=List[:mid]
        RightList=List[mid:]
        MergeSort(LeftList)
        MergeSort(RightList)


        i=j=k=0

        while i<len(LeftList) and j<len(RightList):
            if LeftList[i]<RightList[j]:
                List[k]=LeftList[i]
                i+=1
            else:
                List[k]=RightList[j]
                j+=1
            k+=1
        while i<len(LeftList):
            List[k]=LeftList[i]
            i+=1
            k+=1
        while j<len(RightList):
            List[k]=RightList[j]
            j+=1
            k+=1  
    return List        


List=[53,23,45,9,50]
Resault=MergeSort(List)
print(Resault)