import csv

with open('PUBLIC_YESTBID_201706130000_20170614040522.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
