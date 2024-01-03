# #BUBBLE SORT

# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n-1):   #because of only happening the n-1 passes in the n elements of an array
#         flag=0 #this is adding to make adaptive algorithm,if someone given already sorted array we dont want to sort again that why we only done first pass the check it the condition 
#         for j in range(n-i-1): #we want comparisons upto including the count of len(arr)-perticular pass value,but here zero also the we take it as less than
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 flag=1  #if there is no swap done,then the array is already sorted ,if one swap done it is not sorted
#         if flag==0:
#             break
#     # return arr


# array=[4,3,5,2,1]
# bubble_sort(array)
# print(array)


# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         flag=0
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 flag=1
#     if (flag==0):
#         break
#     return arr

# k=bubble_sort([3,2,4,5,2,1])
# print(k)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            

# #INSERTION SORT

# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):#here we want to compare the values from the second index ,thats why.we compare values with previous one an so on
#         j=i-1        #we want to start searching from previous one
#         x=arr[i]
#         while (j>-1 and x < arr[j]):#we only want value comparing upto index 0
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=x  #reason for using j+1 here is every time we minusing the j so we want to get this into the infront of that

# array=[4,3,5,2,1]
# insertion_sort(array)
# print(array)      

# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         x=arr[i+1]
#         j=i
#         while j>=0 and arr[j]>x:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=x
#     return arr


# x=insertion_sort([5,3,2,4,1])
# print(x)
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#SELECTION SORT

# def selection_sort(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         k=i
#         for j in range(i,n):
#             if arr[k]>arr[j]:
#                 k=j
#         arr[i],arr[k]=arr[k],arr[i]
# array=[4,3,5,2,1]
# selection_sort(array)
# print(array)

# def selection_sort(arr):
#     n=len(arr)
    
#     for i in range(n-1):
#         k=i
#         for j in range(i,n):
#             if arr[k]>arr[j]:
#                 k=j
#         arr[i],arr[k]=arr[k],arr[i]

#     return arr

# k=selection_sort([5,3,4,2,1])
# print(k)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# #QUICK SORT---1st method

# def quick_sort(arr,left,right):
#     if left<right:
#         partition_position=partition(arr,left,right)
#         quick_sort(arr,left,partition_position)
#         quick_sort(arr,partition_position+1,right)



# def partition(arr,left,right):
#     i=left
#     j=right-1
#     pivote=arr[right]
#     if i<j:
#         while i<right and arr[i]<pivote:
#             i+=1
#         while j>left and arr[j]>=pivote:
#             j-=1
#         if i<j:
#             arr[i],arr[j]=arr[j],arr[i]
#     if arr[i]>pivote:
#         arr[i],arr[right]=arr[right],arr[i]
#     return i

# array=[4,3,5,2,1]
# quick_sort(array,0,len(array)-1)
# print(array)

# def quick_sort(arr,left,right):
#     if left<right:
#         partition_position=partition(arr,left,right)
#         quick_sort(arr,left,partition_position)
#         quick_sort(arr,partition_position+1,right)

# def partition(arr,left,right):
#     pivote=arr[right]
#     high=right-1
#     low=left
#     if low<high:
#         while low<right and arr[low]<pivote:
#             low+=1
#         while high>left and arr[high]>=pivote:
#             high-=1
#         if low<high:
#             arr[low],arr[high]=arr[high],arr[low]
#     if arr[low]>pivote:
#         arr[low],arr[right]=arr[right],arr[low]
#     return low

# array=[4,3,5,2,1]
# quick_sort(array,0,len(array)-1)
# print(array)

#-------------------------------------------------------------------------------------------
#SIMPLE QUICK SORT

# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         pivote=arr[0]
#         greater_elements=[x for x in arr[1:] if x>pivote]
#         less_elements=[x for x in arr[1:] if x<=pivote]
#         return quick_sort(less_elements)+ [pivote] +quick_sort(greater_elements)


# array=[4,3,5,2,1]
# array=quick_sort(array)
# print(array)


#-------------------------------------------------------------------------------------------

# # #MERGE SORT (wrong)

# def merge(arr,l,mid,h):
#     i=l
#     j=mid+1
#     k=l
#     B=[]
#     while i<=mid and j<=h:
#         if arr[i]<arr[j]:
#             B.append(arr[i])
#             # k+=1
#             i+=1
#         else:
#             B.append(arr[j])
#             i+=1
#     for i in range(i,i<=mid):
#         B.append(arr[i])
#     for j in range(j,j<=h):
#         B.append(arr[j])
    
#     arr=B


# def merge_sort(arr,n):
#     passes=2
#     while passes<=n+1:
#         i=0
#         while i+passes-1<n:
#             l=i
#             h=i+passes-1
#             mid=(l+h)//2
#             merge(arr,l,mid,h)
#             i=i+passes
#         passes=passes*2
        
#     if (passes/2)<n:
#         merge(arr,0,passes/2,n-1)

# array=[4,3,5,2,1]
# merge_sort(array,len(array)-1)
# print(array)

#-----------------------------------------------------------------------

# #MERGE SORT

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i, j, k = 0, 0, 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# Example usage:
# my_array = [4,3,5,2,1]
# merge_sort(my_array)
# print(my_array)

#-------------------------------------------------
#--------------------------------------------------------
# def bubble_sort(arr):
#     length=len(arr)
#     for i in range(1,length):
#         flag=0
#         for j in range(length-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 flag=1
#         if flag==0:
#             break
#     return arr

# print(bubble_sort([4,5,3,2,1]))

# def insertion_sort(arr):
#     length=len(arr)
#     for i in range(1,length):
#         j=i-1
#         x=arr[i]
#         while j>=0 and arr[j]>x:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=x
#     return arr

# print(insertion_sort([4,5,3,2,1]))


# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         k=i
#         for j in range(i,n):
#             if arr[k]>arr[j]:
#                 k=j
#         arr[i],arr[k]=arr[k],arr[i]
#     return arr

# print(selection_sort([4,5,3,2,1]))


# def quick_sort(arr,left,right):
#     if left<right:
#         partition_position=partition(arr,left,right)
#         quick_sort(arr,left,partition_position)
#         quick_sort(arr,partition_position+1,right)
#     return arr

# def partition(arr,left,right):
#     l=left
#     h=right-1
#     pivote=arr[right]
#     if l<h:
#         while l<right and arr[l]<pivote:
#             l+=1
#         while h>left and arr[h]>=pivote:
#             h-=1
#         if l<h:
#             arr[l],arr[h]=arr[h],arr[l]
#     if arr[l]>pivote:
#         arr[l],arr[right]=arr[right],arr[l]
#     return l

# print(quick_sort([4,5,3,2,1],0,4))


def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i,j,k=0,0,0
        
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<=right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            k+=1
            j+=1
    return arr


print(merge_sort([4,5,3,2,1]))

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i, j, k = 0, 0, 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1