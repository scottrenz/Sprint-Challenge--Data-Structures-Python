import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
alln =  names_1 + names_2
def merge( arrA, arrB ):
    #elements = len( arrA ) + len( arrB )
    #merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    while arrA != [] and arrB != []:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            if len(arrA) == 1:
                arrA = []
            else:    
                arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            if len(arrB) == 1:
                arrB = []
            else:    
                arrB = arrB[1:]
    while arrA != []:
        merged_arr.append(arrA[0])
        arrA.pop(0)
        # if len(arrA) == 1:
        #     arrA = []
        # else:    
        #     arrA = arrA[1:]
    while arrB != []:
        merged_arr.append(arrB[0])
        arrB.pop(0)
        # if len(arrB) == 1:
        #     arrB = []
        # else:    
        #     arrB = arrB[1:]
    return merged_arr

def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    left = merge_sort(left)
    right =merge_sort(right)
    arr = merge(left,right)
    return arr
    
x = ''
for v in merge_sort(alln):
    if v == x:
        duplicates.append(v)
    x = v    

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
