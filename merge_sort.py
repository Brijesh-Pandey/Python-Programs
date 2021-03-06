li=[int(x)for x in input().split()]
def merge(li1,li2,li):
    i,j,k=0,0,0
    while i<len(li1) and j<len(li2):
        if li1[i]<li2[j]:
            li[k]=li1[i]
            i=i+1
            k=k+1
        else:
            li[k]=li2[j]
            j=j+1
            k=k+1
    while i<len(li1):
        li[k]=li1[i]
        i=i+1
        k=k+1
    while j<len(li2):
        li[k]=li2[j]
        j=j+1
        k=k+1

def merge_sort(li):
    if len(li)==0 or len(li)==1:
        return
    mid=len(li)//2
    li1=li[:mid]
    li2=li[mid:]
    merge_sort(li1)
    merge_sort(li2)
    merge(li1,li2,li)
merge_sort(li)
print(li)
