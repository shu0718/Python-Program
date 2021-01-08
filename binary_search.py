def binary_search(list,n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            pos = mid
            return pos
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
list = [23,45,66,299,2099,4999900]
n = 66
a = binary_search(list,n)
print("{} is present in the given list at this position {}".format(n,a))

