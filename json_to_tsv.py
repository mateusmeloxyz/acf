import json
import csv
import re

# input data
json_file = open("acf.json", "r")
json_string = json_file.read()
#json_string = re.sub(r'/\ufeff/g','', json_string)
decoded_data = json_string.encode().decode('utf-8-sig')
json_data = json.loads(decoded_data)
json_file.close()

tsv_file = open("acf.tsv", "w")
#tsv_writer = csv.writer(tsv_file, delimiter='\t')

#tsv_writer.writerow(data[0].keys()) # write the header

for book in enumerate(json_data): # write data rows
    for chapter in enumerate(book[1]['chapters']):
        for verse in enumerate(chapter[1]):
            tsv_file.write("{}\t{}\t{}\t{}\t{}\t{}\t".format(book[1]['name'], book[1]['abbrev'], book[0]+1, chapter[0]+1, verse[0]+1, verse[1]))
            tsv_file.write('\n')

tsv_file.close()