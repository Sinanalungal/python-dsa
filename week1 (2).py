#FIBONACCI

# def fibonacci(n):
#     a=[0,1]
#     if n<0:
#         print('Enter a valid input')
#     elif n==1 or n==2:
#         if n==1:
#             return a[:1]
#         else:
#             return a
#     else:
#         for _ in range(2,n):
#             b=a[-1]+a[-2]
#             a.append(b)
#         return a
    
# print(fibonacci(10))


# def f(n,a=0,b=1):
#     if n > 0:
#         print(a, end=" ")
#         f(n-1, b, a+b)
#     return ''

# print(f(6))        

#----------------------------------------------
#FACTORIAL
# def fact(n):
#     if n>=0:
#         if n==0 or n==1:
#             return 1
#         else:
#             return n*fact(n-1)
#     else:
#         return 'enter a valid one'
    
# print(fact(0))

#-----------------
# h='sinan'

# def reverse(s):
#     if s!='':
#         for i in s:
#             return s[-1]+reverse(s[0:-1])
#     else:
#         return ''
    
# print(reverse(h))

# def sum_of_numbers(n):
#     if n>=0:
#         if n==0:
#             return 0
#         else:
#             return n+sum_of_numbers(n-1)
#     else:
#         if n==0:
#             return 0
#         else:
#             return n+sum_of_numbers(n+1)


# print(sum_of_numbers(100))


#-------------------------------------------------------
#BINARY SEARCH USING RECURSION
# from math import floor
# array=[1,2,3,4,5,6]

# def binary_search(arr,key,h,l=0):
#     if l<=h:
#         arr.sort()
#         mid =(l+h)//2
#         if key==arr[mid]:
#             return f"Position is : {mid}"
#         elif key<arr[mid]:
#             return binary_search(arr,key,mid-1,l)
#         elif key > arr[mid]:
#             return binary_search(arr,key,h,mid+1,)
#     else:
#         return 'Not found'
# print(binary_search(array,100,h=len(array)-1))

#--------------------------------------------------------------

#BINARY SEARCH WITHOUT RECURSION

# def binary_search(array,key):
#     array.sort()
#     l=0
#     h=len(array)
#     Test=True
    
#     while Test and l<=h:
#         mid=(l+h)//2
#         if array[mid]==key:
#             Test=False
#             return f"key found at {mid}" 
#         elif key<array[mid]:
#             h=mid-1
#         else :
#             l=mid+1
#     if Test is True:
#         return 'There is no element in this'


# print(binary_search([2,3,5,4],2))



# def counts(string,found):
#     length=len(string)
#     length2=len(found)
#     i=0
#     count=0
#     while i<= (length-length2):
#         if string[i:i+length2]==found:
#             count+=1
#             i=i+length2
#         else:
#             i+=1
#     return count

# c=counts('bromybbro',"bro")
# print(c)


#flattenig of an array

# def flattening(arr):
#     flatted=[]
#     for i in arr:
#         if isinstance(i,list):
#             flatted.extend(flattening(i))
#         else:
#             flatted.append(i)
#     return flatted

# nested_array = [[[[2, 3]], [4, 5]], [6, 7], [[8, 9], 10]]
# result = flattening(nested_array)
# print(result)



