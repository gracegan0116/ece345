# Insertion Sort
import csv


def insertion_sort(file):
    csv_data = []

    # stores csv file to dict
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_data.append(row)

    # insertion sort
    for i in range(1, len(csv_data)):
        (sort_key, values) = (csv_data[i][0], csv_data[i])
        j = i - 1
        while j >= 0 and csv_data[j][0] > sort_key:
            csv_data[j+1] = csv_data[j]
            j -= 1
        csv_data[j+1] = values

insertion_sort('a1.small.csv')