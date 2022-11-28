# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")

# must be in-place sort
def merge_sort(arr,cmp):
    #pass
    if len(arr) > 1:
        i = 0
        j = 0
        k = 0
        half = len(arr)//2
        leftSide = arr[:half]
        rightSide = arr[half:]

        merge_sort(leftSide)
        merge_sort(rightSide)

        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] <= rightSide[j]:
                arr[k] = leftSide[i]
                i = i + 1

            else:
                arr[k] = rightSide[j]
                j = j + 1

            k = k + 1

        while i < len(leftSide):
            arr[k] = leftSide[i]
            i = i + 1
            k = k + 1

        while j < len(rightSide):
            arr[k] = rightSide[j]
            j = j + 1
            k = k + 1

# must be in-place sort
def quick_sort(arr,cmp):
    pass
