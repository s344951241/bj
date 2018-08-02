#!/user/bin/python
# -*- coding:UTF-8 -*-
import copy
import os
def merge(arr,left,mid,right,temp):
	i = left
	j = mid+1
	t = 0
	while(i<=mid and j<=right):
		if(arr[i]<=arr[j]):
			temp[t] = arr[i]
			t+=1
			i+=1
		else:
			temp[t] = arr[j]
			t+=1
			j+=1
	while(i<=mid):
		temp[t] = arr[i]
		t+=1
		i+=1
	while(j<=right):
		temp[t] = arr[j]
		t+=1
		j+=1
	t = 0
	while(left<=right):
		arr[left] = temp[t]
		left+=1
		t+=1

def sort(arr,left,right,temp):
	if(left<right):
		mid = (left+right)/2
		sort(arr,left,mid,temp)
		sort(arr,mid+1,right,temp)
		merge(arr,left,mid,right,temp)

arr = [9,8,7,6,5,4,3,2,1]
temp = copy.deepcopy(arr)
sort(arr,0,len(arr)-1,temp)
print(arr)
os.system("pause")
