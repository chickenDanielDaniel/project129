import csv
dataset1 = []
dataset2 = []

with open("","r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        dataset1.append(i)


with open("","r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        dataset2.append(i)

headers1 = dataset1[0]
star_data1 = dataset1[1:]

headers2 = dataset2[0]
star_data2 = dataset2[1:]

headers = headers1+headers2

star_data = []

for index, data in enumerate(star_data1):
    star_data.append(star_data1[index]+star_data2[index])

with open("","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
