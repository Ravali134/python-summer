#1.by using list as array
#1.finding smallest element in array
# n=int(input())
# a=list(map(int,input().split()))
# s=a[0]
# for i in a:
#     if i<s:
#         s=i
# print(s)

#2.finding largest element in array
# n=int(input())
# a=list(map(int,input().split()))
# s=a[0]
# for i in a:
#     if i>s:
#         s=i
# print(s)

#importing array module to find largest element in aray
# import array as arr
# a=arr.array('i',list(map(int,input().split())))
# s=a[0]
# for i in a:
#     if i>s:
#         s=i
# print(s)

#3.finding second smallest element in array
# n=int(input())
# a=list(map(int,input().split()))
# s=a[0]
# s1=a[1]
# for i in a:
#     if i<s:
#         s=i
#     else:
#         i>s1 and i!=s
# print(s)


#using sort
# n=int(input())
# a=list(map(int,input().split()))
# a.sort()
# print(a[1])

#4.finding second largest element in array
# n=int(input())
# a=list(map(int,input().split()))
# a.sort()
# print(a[-2])

#5.reverse an array
# n=int(input())
# a=list(map(int,input().split()))
# print(a[::-1])

#6.count the frequency of each element in a list
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# dup=[]
# for i in a:
#     if i not in dup:
#         print(i,a.count(i))
#         dup.append(i)

#7.remove duplicates in a array while maintaining insertiion order
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# dup=[]
# for i in a:
#     if i not in dup:
#         dup.append(i)
# print(dup)
#      (or)
#using set
# n=int(input())
# a=list(map(int,input().split()))
# c=list(set(a))
# print(c)

#8.Rotate the array to the right by k postions
# n=int(input())
# a=list(map(int,input().split()))
# k=int(input())
# print(a)
# # print(a[-k:])
# # print(a[:k+1])
# #    (or)
# print(a[-k:]+a[:-k])

#9.find the Repeating Elements
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# dup=[]
# for i in a:
#     if i not in dup:
#         dup.append(i)
#     else:
#         print(i,end=" ")

#     
#10.find the non Repeating elemnts 
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# dup=[]
# for i in a:
#     if i not in dup:
#         dup.append(i)
# print(dup)

#11.find the equilibrium element where left and right sum is same
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# for i in a:
#     l=sum(a[i:])
#     r=sum(a[:i+1])
#     if l==r:
#         print(i)
#         break

#12.maximum sub array
# n = int(input())
# a = list(map(int, input().split()))
# max_sum = a[0]
# for i in range(n):
#     current_sum = 0
#     for j in range(i, n):
#         current_sum += a[j]
#         if current_sum > max_sum:
#             max_sum = current_sum

# print(max_sum)


#13.find the median of the array
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# a.sort()
# if n%2==0:
#     print(a[n//2-1])
# else:
#     print(a[n//2])

#14.check whether second array is subset of first array
# n1=int(input())
# a=list(map(int,input().split()))
# n2=int(input())
# b=list(map(int,input().split()))
# for i in b:
#     if i in a:
#         print("Yes")
#         break
#     else:
#         print("no")
#         break 

        #(or)
# n1=int(input())
# a=list(map(int,input().split()))
# n2=int(input())
# b=list(map(int,input().split()))
# f=True
# for i in b:
#     if i in a:
#       pass
#     else:
#         f=False
#         break
# if f==True:
#     print("yes")
# else:
#     print("no") 


#15.search an element is present or not
# n=int(input())
# a=list(map(int,input().split()))
# k=int(input())
# for i in a:
#     if k in a:
#         print("found")
#         break
#     else:
#         print("not found")
#         break
     #(or)
# n=int(input())
# a=list(map(int,input().split()))
# k=int(input())
# for i in a:
#     if i==k:
#         print("found")
# else:
#     print("not found")

#16.symmetric pairs
n = int(input())
pairs = []
for i in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))
for i in range(n):
    for j in range(i , n):
        if pairs[i][0] == pairs[j][1] and pairs[i][1] == pairs[j][0]:
            print(pairs[i])


#17. one number missing number from 1 to n
# n=int(input())
# a=list(map(int,input().split()))
# n=len(a)+1
# ep=n*(n+1)//2
# c=sum(a)
# r=ep-c
# print(r)
     #(or)
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# b=len(a)
# for i in range(1,b+1):
#     if i not in a:
#         print(i,end=" ")

#18.find all leader of an array
# n=int(input())
# a=list(map(int,input().split()))
# print(a)
# for i in range(len(a)):
#     if a[i]==max(a[i:]):
#         print(a[i],end=" ")

#19.pair sum
# n=int(input())
# a=list(map(int,input().split()))
# k=int(input())
# for i in range(len(a)):
#     for j in range(i,len(a)-1):
#         if a[i]+a[j]==k:
#             print(a[i],a[j])
#             break

#20union and intersection of array
# n1=int(input())
# a=list(map(int,input().split()))
# n2=int(input())
# b=list(map(int,input().split()))
# print(a)
# print(b)
# print("union:"*(set(a)&set(b)))
# print("intersection:"*(set(a)|set(b)))


