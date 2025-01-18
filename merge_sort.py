#Merge sort module

def merge_sort(arr):

    #base case
    if len(arr)<=1:
        print(arr)
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    merged = []

    Lcount = len(left)
    Rcount = len(right)
    Lindex = 0
    Rindex = 0
    
    while Lindex < Lcount and Rindex < Rcount:

        if left[Lindex] <= right[Rindex]:
            merged.append(left[Lindex])
            Lindex += 1
            
            
        else:
            merged.append(right[Rindex])
            Rindex += 1
            

    print('\n')
    
    while Lindex < Lcount:
        merged.append(left[Lindex])
        Lindex += 1

    while Rindex < Rcount:
        merged.append(right[Rindex])
        Rindex += 1        
    
    return merged
    
