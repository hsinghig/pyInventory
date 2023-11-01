import csv

def writer(header, data, filename, option):
    with open(filename, "w", newline="") as csvfile:
        if option == "write":
            filecsvWriter = csv.writer(csvfile)
            filecsvWriter.writerow(header)
            for x in data:
                filecsvWriter.writerow(x)
        elif option == "update":
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
        else:
            print("Option is not known available options are write/update")

def updater(filename):
    with open(filename, newline="") as csvfile:
        readData = [row for row in csv.DictReader(csvfile)]
        print(readData)
        readData[0]['Rating'] = '9.4'
    
    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")


if __name__ == '__main__':
    filename = 'app//data//test.csv'
    header = ('Rank', 'Rating', 'Title')
    data = [
        (1, 8, 'The Matrix'), (1, 7, 'The Matrix Reloaded'), (1, 5, 'The Matrix Revolutions'), (1, 6, 'The Matrix Resurrections')
    ]
    writer(header, data, filename, "write")
    updater(filename=filename)