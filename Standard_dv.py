import csv

with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data=file_data[0]
def mean(data):
    n=len(data)