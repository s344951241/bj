#!/user/bin/python
# -*- coding:UTF-8 -*-

import os

def quickSort(data):
	sort(data,0,len(data)-1)
	return data

def sort(data,lo,hi):
	if hi<=lo:
		return
	j = partition(data,lo,hi)
	sort(data,lo,j-1)
	sort(data,j+1,hi)

def partition(data,lo,hi):
	key = hi
	while lo<hi:
		while ((lo<hi) and (data[lo]<=data[key])):
			lo= lo+1
		while ((lo<hi) and (data[hi]>=data[key])):
			hi = hi-1
		exch(data,lo,hi)
	exch(data,lo,key)
	return lo

def exch(data,lo,hi):
	temp = data[lo]
	data[lo] = data[hi]
	data[hi] = temp


nums = [9,2,5,8,2,7,1]
print(quickSort(nums))

os.system("pause")