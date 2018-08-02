#!/user/bin/python
# -*- coding:UTF-8 -*-

import os
def shellSort(arr):
	increment = len(arr)
	while increment>1:
		increment = increment/3+1
		for i in range(increment,len(arr)):
			key = arr[i]
			j = i-increment
			while j>=0:
				if key<arr[j]:
					temp = arr[j]
					arr[j]=key
					arr[j+increment] = temp
				j=j-increment
	return arr

nums = [9,2,5,8,2,7,1]
print(shellSort(nums))

os.system("pause")
