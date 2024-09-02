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

#Goal: mimic input for npiet for running code
#Currently from Gabriella Singh Cadieux
default_palette = {
    'maxval' : '255',
    'W' : '255 255 255',
    'B' : '0 0 0',
    '1A' : '255 192 192' , '2A' : '255 255 192' , '3A' : '192 255 192' , '4A' : '192 255 255' , '5A' : '192 192 255' , '6A' : '255 192 255' ,
    '1B' : '255 0 0'     , '2B' : '255 255 0'   , '3B' : '0 255 0'     , '4B' : '0 255 255'   , '5B' : '0   0   255' , '6B' : '255 0 255' ,
    '1C' : '192 0 0'     , '2C' : '192 192 0'   , '3C' : '0 192 0'     , '4C' : '0 192 192'   , '5C' : '0   0   192' , '6C' : '192 0 192' 
}

#Mimic input for npiet with sli
default_palette_adjusted = {
    'maxval' : '255',
    'W' : '255 255 255',
    'B' : '0 0 0',
    '1A' : '255 200 200' , '2A' : '255 255 200' , '3A' : '180 255 180' , '4A' : '200 255 255' , '5A' : '200 200 255' , '6A' : '255 200 255' ,
    '1B' : '255 0 0'     , '2B' : '255 255 0'   , '3B' : '0 255 0'     , '4B' : '0 255 255'   , '5B' : '0   0   255' , '6B' : '255 0 255' ,
    '1C' : '200 0 0'     , '2C' : '220 200 0'   , '3C' : '0 200 0'     , '4C' : '0 200 200'   , '5C' : '0   0   200' , '6C' : '200 0 200' 
}

#https://coolors.co/palette/01befe-ffdd00-ff7d00-ff006d-adff02-8f00ff
modern_palette_standard = {
    'maxval' : '255',
    'W' : '255 255 255',
    'B' : '0 0 0',
    #Raspberry            #Orange               #Yellow               #Lime                 #Cyan                 #Purple
    '1A' : '255 120 230', '2A' : '255 200 140', '3A' : '255 240 136', '4A' : '215 255 132', '5A' : '145 227 255', '6A' : '203 138 255',
    '1B' : '255   0 109', '2B' : '255 125 0'  , '3B' : '255 221 0'  , '4B' : '173 255   2', '5B' : '  1 190 255', '6B' : '143   0 255',
    '1C' : '200   0  85', '2C' : '200 100 0'  , '3C' : '200 170 0'  , '4C' : '136 200   0', '5C' : '  1 150 200', '6C' : '102   0 180' 
}

#Convert csv to rgb codes
palette = default_palette
#palette = modern_palette_standard
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
