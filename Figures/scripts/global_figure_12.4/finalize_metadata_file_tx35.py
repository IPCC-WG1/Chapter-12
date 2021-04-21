import csv


metadata_input_filename = '/home/jservon/Chapter12_IPCC/data/Figure_12.4/tx35/CMIP6_day_tx35isimip.csv'

output_metadata_filename = '/home/jservon/Chapter12_IPCC/data/Figure_12.4/tx35/CMIP6_day_tx35isimip_withpanels.csv'

rows = []
with open(metadata_input_filename) as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         newrow = row[0].replace('"','')
         if 'ssp126' in row[0]:
            newrow = row[0].replace('"','')+',a'
         if 'historical' in row[0]:
            newrow = row[0].replace('"','')+',a,b,c'
         if 'ssp585' in row[0]:
            newrow = row[0].replace('"','')+',b,c'
         finalrow = newrow.split(',')[1:]
         if 'DATA_REF_SYNTAX' in newrow:
             finalrow.append('panels')
         rows.append(finalrow)
         #    #print newrow.split(',')[1:].join(',')+',panels'
         #    print ','.join(newrow.split(',')[1:])+',panels'
         #else:
         #    print ','.join(newrow.split(',')[1:])
         #print(', '.join(row))

with open(output_metadata_filename, 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in rows:
        spamwriter.writerow(row)

