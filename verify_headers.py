import sys
from os import listdir
from os.path import isfile, join

txt_file_loc = sys.argv[1]
all_files = listdir(txt_file_loc)
txt_paths = [txt_file_loc + f for f in all_files if isfile(join(txt_file_loc, f))]

headers_file_name = sys.argv[2]


headers_file = open( headers_file_name, "r" )

headers = headers_file.readlines()
headers_list = [header.strip() for header in headers ]

not_found = False
for txt_path in txt_paths:
	rain_file = open( txt_path, "r")
	lines = rain_file.read()
	for header in headers_list:
		if lines.find(header) < 0:
			not_found = True
			print(header + " was not found in: " + txt_path)
	rain_file.close

if not_found == False:
	print("No mismatches found!\n")

headers_file.close()



