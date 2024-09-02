import csv
from PIL import Image as image

input_file_name = 'sample.csv'
output_file_name = 'sample.ppm'

output_to_png = True
secondary_output_file_name = 'sample.png'

#Read input_csv
input_csv = []
with open(input_file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')
    for row in csv_reader:
        input_csv.append([])
        for cell in row:
            input_csv[-1].append(cell)

print(input_csv)

default_palette = {
    'maxval' : '3',
    'W' : '3 3 3',
    'B' : '0 0 0',
    '1A' : '3 0 0' , '1B' : '2 0 0' , '1C' : '1 0 0' ,
    '2A' : '3 3 0' , '2B' : '2 2 0' , '2C' : '1 1 0' ,
    '3A' : '0 3 0' , '3B' : '0 2 0' , '3C' : '0 1 0' ,
    '4A' : '0 3 3' , '4B' : '0 2 2' , '4C' : '0 1 1' ,
    '5A' : '0 0 3' , '5B' : '0 0 2' , '5C' : '0 0 1' ,
    '6A' : '3 0 3' , '6B' : '2 0 2' , '6C' : '1 0 1' ,
}

default_palette = {
    'maxval' : '255',
    'W' : '255 255 255',
    'B' : '0 0 0',
    '1A' : '255 200 200' , '2A' : '255 255 200' , '3A' : '180 255 180' , '4A' : '200 255 255' , '5A' : '200 200 255' , '6A' : '255 200 255' ,
    '1B' : '255 0 0'     , '2B' : '255 255 0'   , '3B' : '0 255 0'     , '4B' : '0 255 255'   , '5B' : '0   0   255' , '6B' : '255 0 255' ,
    '1C' : '200 0 0'     , '2C' : '220 200 0'   , '3C' : '0 200 0'     , '4C' : '0 200 200'   , '5C' : '0   0   200' , '6C' : '200 0 200' 
}

#Convert csv to rgb codes
palette = default_palette
input_csv = [[palette[cell] for cell in row] for row in input_csv]

#input_csv = map(input_csv, lambda row : map(row, lambda cell : palette[cell]))
print(input_csv)

#Output to ppm format
file_width = max(map(len, input_csv))
file_height = len(input_csv)

with open(output_file_name, 'w') as ppm_file:
    ppm_file.write('P3\n')
    dimension_string = str(file_width) + ' ' + str(file_height) + '\n'
    ppm_file.write(dimension_string)
    ppm_file.write(str(palette['maxval']) + '\n')
    for row in input_csv:
        for cell in row:
            ppm_file.write(cell)
            ppm_file.write('\n')

if output_to_png:
    im = image.open(output_file_name)
    im.save(secondary_output_file_name)
