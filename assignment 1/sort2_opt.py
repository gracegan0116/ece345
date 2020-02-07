# Merge Sort
import csv
import sys
import time


def csv_to_list(file):
    csv_list = []
    # stores csv file to list
    with open(file, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_list.append(row)
    return csv_list


def merge(arr, left, mid, right):
    start = mid+1
    if int(arr[mid][0]) <= int(arr[start][0]):
        return

    while left <= mid and start <= right:
        if int(arr[left][0]) <= int(arr[start][0]):
            left += 1
        else:
            value = arr[start]
            index = start
            while index != left:
                arr[index] = arr[index-1]
                index = index - 1
            arr[left] = value

            left += 1
            mid += 1
            start += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left+right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


if __name__ == "__main__":
    inputfile = 'a1.large'
    csv_data = csv_to_list(inputfile + '.csv')
    start_time = time.time()
    merge_sort(csv_data, 0, len(csv_data) - 1)
    print("My program took", time.time() - start_time, "to run")
    # for item in csv_data:
    #     print(item)
