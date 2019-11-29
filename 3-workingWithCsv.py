import csv

def readCSV(filename):
    return list(csv.DictReader(open(filename, 'r')))

def writeCsvWithoutOrder(rows, fileName):
    keys = rows[0].keys()
    with open(fileName, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(rows)
    return fileName


def writeCsvWithOrder(rows, fileName):
    keys = ['a', 'b', 'c']
    with open(fileName, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(rows)
    return fileName

data = [
    {
        "b" : 1,
        "c" : 3,
        "a" : 5
    },
    {
        "b": 10,
        "c": 3,
        "a": 15
    },
    {
        "b": 14,
        "c": 37,
        "a": 5
    }
]

writeCsvWithoutOrder(data,'writeWithoutOrder.csv')
writeCsvWithOrder(data, 'writeWithOrder.csv')
