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
                  
if __name__ == "__main__":
