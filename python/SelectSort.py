#!/user/bin/python
# -*- coding:UTF-8 -*-

import os

def selectSort(data):
	N = len(data)
	for i in range(0,N):
		min = i
		for j in range(i+1,N):
			if data[j]<data[min]:
				min = j
		temp = data[i]
		data[i] = data[min]
		data[min] = temp
	return data
nums = [9,2,5,8,2,7,1]
print(selectSort(nums))

os.system("pause")