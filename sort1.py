# Insertion Sort
import csv
import sys


def csv_to_list(file):
    csv_list = []
    # stores csv file to list
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_list.append(row)
    return csv_list


def insertion_sort(arr):
    for i in range(1, len(arr)):
        (sort_key, values) = (arr[i][0], arr[i])
        j = i - 1
        while j >= 0 and int(arr[j][0]) > int(sort_key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = values


if __name__ == "__main__":
    inputfile = (sys.argv[1])
    csv_data = csv_to_list(inputfile + '.csv')
    insertion_sort(csv_data)
    for item in csv_data:
        print(item)
