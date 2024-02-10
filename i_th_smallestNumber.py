def select(List,first,last,i):
    if first==last: 
        return List[first]
    q=partition(List,first,last)
    k=q-first+1
    if k==i:
        return List[q]
    elif i<k:
        x=select(List,first,q-1,i)
    else:
        x=select(List,q+1,last,i-k)    
    return x

def partition(List,first,last):
    pivot=List[first]
    i=first+1
    j=last
    while i<=j:
        while List[i]<pivot:
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

List=[1,1,2,3,4,86,34,65,-22,12,17,13,7,89,76]
List=list(set(List))
i=7
resault=select(List,0,len(List)-1,i)
print(resault)