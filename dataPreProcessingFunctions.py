def dataPreProcessing(txtPaths, csvPaths):
	ENTIDAD = "ENTIDAD"
	RECORD_SIZE = 14
	#Processing the .txt files and converting them into .csv ones
	for txtpath, csvpath in zip(txtPaths, csvPaths):
		rain_file = open( txtpath )
		lines = rain_file.readlines()
		csv_lines = []
		
		#eliminating any additional comma or whitespace, leaving headers and values only 
		entidadFound = False
		for index, line in enumerate(lines):
			line = line.replace( ",","" )
			line = line.replace( '\n',"" )
			line = line.replace( '\r',"" )
			line = line.replace( "\n\r","" )
			line = line.strip()
			if len( line ) > 0:
				if line[0].isalpha():
					line = line.upper()
				if line == ENTIDAD:
					entidadFound = True
				if line != ENTIDAD and not entidadFound: #highly dependant of the txt file
					line=""
			lines[index] = line

		#moving only the values to a different list
		actualValues = []
		for line in lines:
			if len(line) > 0 and ( line[0].isalpha() or line[0].isnumeric() ):
				actualValues.append( line )

		#formating the values to add them a comma or a new-line character 
		recordMark = 1;
		for index, value in enumerate(actualValues):
			if recordMark%RECORD_SIZE == 0:
				actualValues[index] = value + "\n"
			else:
				actualValues[index] = value + ","
			recordMark = recordMark + 1
		
		#writting the values to a .csv files
		rainCSVFile = open( csvpath, "w" )
		for value in actualValues:
			rainCSVFile.write( value )
		rainCSVFile.close()
