import csv

csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/cleanme-clean.csv', 'w')

# Now a DictReader and DictWriter
# DictReader and DictWriter are imported libraries
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)
# DictWriter writes to outfile
#reader.fieldname refers to the headers

# Write headers
writer.writeheader()

# Clean and write the data to output
#for row in reader:
    #row['first_name'] = row['first_name'].upper()
    #row["zip"]=row["zip"].zfill(5)
    #row['city'] = row['city'].replace('&nbsp;', '_')
    #if int(row['amount']) > 1000.0: 
        #writer.writerow(row)
for row in reader:
    row["first_name"]=row["first_name"].upper()
    row["zip"]=row["zip"].zfill(5)
    row['city'] = row['city'].replace('&nbsp;', '_')
    if int(row['amount']) >= 1000:
        writer.writerow(row)
