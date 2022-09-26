import csv
data = []

with open("","r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data.append(i)

headers = data[0]
star_data = data[1:]

for i in planet_data:
    i[2] = i[2].lower()

star_data.sort(key = lambda planet_data:planet_data[2])

with open("","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
