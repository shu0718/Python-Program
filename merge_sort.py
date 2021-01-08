def mergesort(lst1):
    mid = len(lst1)//2
    if mid >= 1:    
        left_lst = lst1[:mid]
        right_lst = lst1[mid:]
        mergesort(left_lst)
        mergesort(right_lst)
        i = 0
        j = 0
        k = 0
        while i<len(left_lst) and j<len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst1[k] = left_lst[i]
                i+=1
                k+=1
            else:
                lst1[k] = right_lst[j]
                j+=1
                k+=1
        while i<len(left_lst):
            lst1[k] = left_lst[i]
            i+=1
            k+=1
        while j<len(right_lst):
            lst1[k] = right_lst[j]
            j+=1
            k+=1
        
    
    


size = int(input("Enter the size of an array:"))
lst1 = [int(input())for i in range(size)]
mergesort(lst1)
print(lst1)

    
