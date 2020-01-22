import csv
import sys

def flip(arr, i):
    left = 0
    right = i
    while left <= right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right]=temp
        left = left + 1
        right = right - 1

def findMax(arr, length):
    max = 0
    for i in range(1, length):
        if int(arr[i][0]) > int(arr[max][0]):
            max = i
    return max


def pancakeSort(arr):
    length = len(arr)
    while length >= 1:
        maximum = findMax(arr, length)
        if maximum != length-1:
            flip(arr, maximum)
            flip(arr, length-1)
        length = length - 1
    


if __name__ == "__main__":
    inputfile = (sys.argv[1])
    with open(inputfile+'.csv','r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        arr = list()
        for row in spamreader:
            arr.append(row)
    result = ['911','215455426']
    pancakeSort(result)
    for i in range (0,len(arr)):
        print(arr[i][0])
    
