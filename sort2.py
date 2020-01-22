# Merge Sort
import csv
import sys


def csv_to_list(file) -> list:
    csv_list = []
    # stores csv file to list
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_list.append(row)
    return csv_list


def merge(arr, left, mid, right):
    # splits arr into 2 temp lists
    left_list = arr[left:mid+1]
    right_list = arr[mid+1:right+1]
    # merge temp lists back to arr
    i, j = 0, 0
    k = left
    while i < len(left_list) and j < len(right_list):
        if left_list[i][0] <= right_list[j][0]:
            arr[k] = left_list[i]
            i += 1
        else:
            arr[k] = right_list[j]
            j += 1
        k += 1
    while i < len(left_list):
        arr[k] = left_list[i]
        i += 1
        k += 1
    while j < len(right_list):
        arr[k] = right_list[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left+right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

        
if __name__ == "__main__":
	inputfile = (sys.argv[1])
	csv_data = csv_to_list(inputfile+'.csv')
	merge_sort(csv_data, 0, len(csv_data)-1)
	for item in csv_data:
		print(item)
