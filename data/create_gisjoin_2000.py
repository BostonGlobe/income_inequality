import csv

output = []

def addRow(input, val):
    newRow = []
    for i in input:
        newRow.append(i)

    newRow.append(val)
    output.append(newRow)

with open('csv/raw_2000.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        val = False
        if i == 0:
            val = 'gisjoin2_mod'
        else:	
            gis = row[5]
            val = gis[:3] + '0' + gis[3:5] + '0' + gis[5:]
            print(val)
        addRow(row, val)        

writer = csv.writer(open('csv/raw_2000_modified.csv', 'w'))
	
for o in output:
   writer.writerow(o)
