#!/usr/bin python
#coding:utf-8

#1 冒泡排序：
def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(i,len(seq)):
            if seq[j] < seq[i]:
                tmp = seq[j]
                seq[j] = seq[i]
                seq[i] = tmp
 
#2 选择排序：
def selection_sort(seq):
    for i in range(len(seq)):
        position = i
        for j in range(i,len(seq)):
            if seq[position] > seq[j]:
                position = j
        if position != i:
                tmp = seq[position]
                seq[position] = seq[i]
                seq[i] = tmp
  
#3 插入排序：
def insertion_sort(seq):
    if len(seq) > 1:
        for i in range(1,len(seq)):
            while i > 0 and seq[i] < seq[i-1]:
                tmp = seq[i]
                seq[i] = seq[i-1]
                seq[i-1] = tmp
                i = i - 1
                
#快速排序：
def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


if __name__ == "__main__":
