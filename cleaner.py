import csv

csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/cleanme-clean.csv', 'w')
#print csvfile.read()

# Now a DictReader and DictWriter
# DictReader and DictWriter are imported libraries
reader = csv.DictReader(csvfile)

# make a new list from reader.fieldnames, but capitalize all the items
#cap_header = []

#for field in reader.fieldnames:
#cap_header.append(field.upper())
#print cap_header

writer = csv.DictWriter(outfile, reader.fieldnames)
#writer = csv.writer(outfile,quoting=csv.QUOTE_ALL)# dialect='excel')
# DictWriter writes to outfile
#reader.fieldname refers to the headers

# Write headers
writer.writeheader()

# Clean and write the data to output
for row in reader:
    for k, v in row.iteritems():
    	if int(row['amount']) >= 1000:
            row[k]=row[k].upper()
            row["zip"]=row["zip"].zfill(5)
            row['city'] = row['city'].replace('&nbsp;', '_')
    writer.writerow(row)

