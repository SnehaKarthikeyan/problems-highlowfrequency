Coding:
  
def maxmin(arr, n):
  arr.sort()
  max_count = 0
  min_count = n
  for i in range(n):
   count=arr.count(arr[i])
   max_count = max(max_count, count)
   min_count = min(min_count, count)
  return min_count,max_count
n = int(input())
arr=list(map(int,input().split()))
a,b=maxmin(arr, n)
print(a,end=" ")
print(b)
