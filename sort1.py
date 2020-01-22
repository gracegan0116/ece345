# Insertion Sort
import csv


def csv_to_list(file) -> list:
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
        while j >= 0 and arr[j][0] > sort_key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = values


csv_data = csv_to_list('a1.small.csv')
insertion_sort(csv_data)
print(csv_data)
