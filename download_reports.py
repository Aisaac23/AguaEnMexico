import requests
import sys
from pathlib import Path

''' 
This script is useful to download multiple files from the same source AND with the name of the files being an increasing number.

The argumnets that must be passed to this script will be:
1. the link to where all the files are stored. Example:
https://smn.conagua.gob.mx/tools/DATA/documents/

2. The starting number. Example: 1985

3. The ending number. Example: 2020

4. The format on which the files are stored. Example: pdf

5. the destination folder where you wnat to save all the files.

'''

OK_CODE = 200
WRITE_MODE = 'wb'
ONE_K = 1000
MIN_SIZE = 50

remote_location = sys.argv[1]

start_number = int(sys.argv[2])
end_number = int(sys.argv[3])


file_format = sys.argv[4]

destination_folder = sys.argv[5]

for index_year in range(start_number, end_number+1):
	name = str(index_year) + '.' + file_format
	url =  remote_location + name 
	
	file_size = 0
	while file_size < MIN_SIZE:
		myfile = requests.get(url)

		downloaded = open(destination_folder+name, WRITE_MODE)
		downloaded.write(myfile.content)
		downloaded.close()

		file_size = Path(destination_folder+name).stat().st_size / ONE_K
	print (name + " downloaded.")
	
