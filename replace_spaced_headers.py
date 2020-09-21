import sys
from os import listdir
from os.path import isfile, join

txt_file_loc = sys.argv[1]
all_files = listdir(txt_file_loc)
txt_paths = [txt_file_loc + f for f in all_files if isfile(join(txt_file_loc, f))]

headers_file_name = sys.argv[2]


headers_file = open( headers_file_name, "r" )

headers = headers_file.readlines()
headers_list = [header.strip() for header in headers]
headers_spaced = [header for header in headers_list if header.find(" ") != -1 ]
headers_dashed = [header.replace(" ", "-") for header in headers_spaced ]

not_found = False

for txt_path in txt_paths:
	rain_file = open( txt_path, "r")
	lines = rain_file.read()
	index = 0
	for header in headers_spaced:
		lines = lines.replace(header, headers_dashed[index], 1)
		index = index+1;
	rain_file.close()
	rain_file = open( txt_path, "w+")
	rain_file.write(lines)
	rain_file.close()

headers_file.close()
