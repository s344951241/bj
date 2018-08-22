#!/user/bin/python
# -*- coding:UTF-8 -*-
# 
import os


def swap(arr,a,b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

def heapSort(arr):
	for i in range(len(arr)/2-1,-1,-1):
		adjustHeap(arr,i,len(arr))
	for j in range(len(arr)-1,0,-1):
		swap(arr,0,j)
		adjustHeap(arr,0,j)

def adjustHeap(arr,i,len):
	temp = arr[i]
   	k = i*2+1
   	while k<len:
    		if k+1<len and arr[k]<arr[k+1]:
    			k=k+1
    		if arr[k]>temp:
    			arr[i] = arr[k]
    			i = k
    		else:
    			break
    	        k=k*2+1
        arr[i] = temp

arr = [9,2,5,8,2,7,1]
heapSort(arr)
print(arr)

os.system("pause")