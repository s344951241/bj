#!/user/bin/python
# -*- coding:UTF-8 -*-

def print_lol(the_list,level):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level)
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)

            
"""注释11234"""


