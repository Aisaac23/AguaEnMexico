import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.widgets import CheckButtons
import matplotlib.patches as mpatches

TXT_EXT, CSV_EXT = ".txt", ".csv"
ENTIDAD = "ENTIDAD"
YEAR, N_YEARS, RECORD_SIZE = 2010, 10, 14
PATH = "/root/Documentos/Python-Projects/Resumenes-Mensuales-de-precipitacion/"
txtPaths, csvPaths = [], []
X_INCHES_LAPTOP = 12
Y_INCHES_LAPTOP = 7
COLORS_LIMIT = 16000000
COLOR_SIZE = 6


mmExplained = "La precipitación pluvial se mide en mm, que sería el espesor de la lámina de agua que se formaría, a causa de la" +  " precipitación, sobre una superficie plana e impermeable y que equivale a litros de agua por metro cuadrado de terreno (l/m^2)."

rainDataFrames = {}
rainDictionaries = {}

figure = plt.figure( constrained_layout=True )
figure.set_size_inches(X_INCHES_LAPTOP + 1, X_INCHES_LAPTOP + 1)
figure.canvas.set_window_title("Precipitación anual de todos los estados de México (interactivo)")
gridSpaceBarChart = figure.add_gridspec(3, 8)
location = figure.add_subplot(gridSpaceBarChart[ : , 1: ]) 
buttonsArea = 	figure.add_subplot(gridSpaceBarChart[1,0])
fillAx = figure.add_subplot(gridSpaceBarChart[2,0])
fillAx.set_axis_off()

yearsDisplayed = []	
constantColors = []

def roundAlwaysUp( toRound, end = 10 ):
	""" 
	This snippet will round-up any given integer or float, to at least 10 or to the highest multiple of 10.
	You can pass an unsigned/positive integer as the "end" argument if you want the number to be rounded to at least a multiple of "end".
	Returned value will always be an integer.
	"""
	if end == 0:
		end = 10
	end = abs( end )
	times = toRound/end
	if times >= 0:
		times = times + 1
	else:
		times = times - 1
	return ( int( times ) )*end; 

def updateBarChart(label):
	location.cla()
	del( yearsDisplayed[:] )

	labels = checks.labels
	for index, checked in enumerate( checks.get_status() ):
		if checked:
			year_checked = labels[index].get_text()
			yearsDisplayed.append( year_checked )
	for year in yearsDisplayed:
		barAllStatesAllYears( int( year ) )

	plt.draw()
	
def barAllStatesAllYears(year=2010):
	N_STATES = 32
	ROTATION_ANGLE = 45
	NACIONAL = "NACIONAL"
	SHRINK_BAR = 0.11
	
	names = []
	both = [location, buttonsArea]
	colors = []

	states = {}
	totals = {}

	states = rainDictionaries[year] # we get a dictionary with the form: {state:{month:amount}} for each year
	for state, value in states.items():
		if state != NACIONAL:
			totals[state] = value["ANUAL"] # we get a dictionary with the form: {state:amount} for the "ANUAL" key
			colors.append( "#"+format( random.randint(0, COLORS_LIMIT), "X" ).zfill(COLOR_SIZE) )
		if len( names ) < N_STATES:
			names.append(state[0:3] + "." + state[-1])
	xPlaces = range( len( totals.keys() ) )
	
	absoluteMax = max( totals.values() )
	absoluteMax = roundAlwaysUp( absoluteMax )
	
	yearsRectangles = []
	shrinkTimes = 0
	if len( yearsDisplayed ) > 1:
		del( colors[:] )
		yLoc = 0
		for index, yd in enumerate( yearsDisplayed ):
			rect = mpatches.Rectangle( [yLoc, 0.001], 0.02, 0.02 )
			idColor = constantColors[index]
			if yd == str (year):
				colors = idColor
				shrinkTimes = index
			rect.set_color( idColor )
			yearsRectangles.append( rect )			
			yLoc = yLoc + 0.025
		

	allBars = location.bar( xPlaces, totals.values(), color = colors, edgecolor='black')#make a 32 colors scale
	
	  
	for singleBar in allBars:
		singleBar.set_width( singleBar.get_width() - SHRINK_BAR*shrinkTimes )	

	location.grid(True)
	location.set_axisbelow(True)
	location.set_xticks(xPlaces) 

	location.set_xticklabels(names, fontsize=10)#pending
	location.set_ylabel( "Valores en milimetros" )
	location.set_ylim(0, absoluteMax)
	location.set_yticks( location.get_yticks() )
	
	location.legend(yearsRectangles ,yearsDisplayed)
	
	formating = " - %s"*( len( yearsDisplayed )-1 )
	figure.suptitle( ( "Precipitación anual en %s" + ( formating ) )%  tuple( yearsDisplayed )  )

	for label in location.get_xticklabels():
		label.set_rotation( ROTATION_ANGLE )
	
	return figure, both

#This function takes the state's name as argument and the range of years and creates and bar chart with the total precipitation per year.
def barTotalPerYear(state, fromYear, toYear):
	ANUAL = "ANUAL"

	totals = {}
	figure, location = plt.subplots(1, 1)

	for key,value in rainDictionaries.items():
		if int(key) >= fromYear and int(key) <= toYear:
			totals[key] = value[state][ANUAL]

	xPlaces = range( len( totals.keys() ) )
	
	absoluteMax = max( totals.values() )
	absoluteMax = roundAlwaysUp( absoluteMax )
	
	location.bar( xPlaces, totals.values(), color = ["#00d9fe", "#2d96ff", "#4568d3"] )
	location.set_axisbelow(True)
	location.grid(True)
	location.set_xticks(xPlaces) 
	location.set_xticklabels(totals.keys(), fontsize=10)
	location.set_ylabel( "Valores en milimetros" )
	location.set_ylim(0, absoluteMax)	
	location.set_yticks( location.get_yticks() )
	figure.suptitle("Precipitación anual en %s"% (state) )
	figure.canvas.set_window_title("Precipitación anual por estado de la república mexicana")
		
	return figure, location

#A line graph of the state indicated, allocating every year we have as data in rows and cols indicated 
def lineAllYearsPerMonth(state, rows, cols):
	years = {}
	ROTATION_ANGLE = 90 #degrees

	for key, value in rainDictionaries.items():
		years[key] = value[state]
	
	figure, location = plt.subplots(rows, cols, constrained_layout = True)	
	#We find the Maximum value of all the years
	absoluteMax = 0
	for value in years.values():
		maxPerState = max( list( value.values() )[0:-1] ) 
		if maxPerState > absoluteMax:
			absoluteMax = maxPerState
	
	absoluteMax = int(absoluteMax)
	absoluteMax = roundAlwaysUp( absoluteMax )

	r, c = 0, 0
	for key, value in years.items():
		months = list( value.keys() )
		mm = list( value.values() )
		if c >= cols:
			c = 0
			r = r+1
		
		location[r, c].plot( months[0:-1], mm[0:-1] )# [0:1] will get all the values but the last one which is the "ANUAL" value
		location[r, c].set_title( str(key) )
		location[r, c].grid(True)
		location[r, c].set_ylim(0, absoluteMax)
		location[r, c].set_yticks( location[r, c].get_yticks() )
		for label in location[r, c].get_xticklabels():
			label.set_rotation( ROTATION_ANGLE )

		c = c+1


	figure.suptitle("Precipitación mensual en %s (%d años)" % (state, len ( rainDictionaries.items() ) ) )
	figure.canvas.set_window_title("Precipitación mensual por estado de la república mexicana")
	figure.set_size_inches(X_INCHES_LAPTOP + 1, X_INCHES_LAPTOP + 1)
	return figure, location

def dataPreProcessing():
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

def createDataFrames():
	#creating a dictionary of dataframes with the years as keys (e.g 2010 -> dataframe_of_2010)
	for index, path in enumerate(csvPaths):
		rainDataFrames[index+YEAR] = pd.read_csv(path)

	#setting the column "ENTIDAD" as index of the dataframe since it'll be easier to iterate by name and all the names are unique.
	#also, we create a dictionary of dictionaries with the following format: year:{"ENTIDAD":{"MONTH":amount}}
	for key, value in rainDataFrames.items():
		rainDictionaries[key] = value.set_index(ENTIDAD).to_dict("index")

#Creating the paths to locate the .txt files and to create the .csv ones
for year in range(YEAR, YEAR+N_YEARS):
	txtPaths.append(PATH + str(year) + TXT_EXT)
	csvPaths.append(PATH + str(year) + CSV_EXT)
	yearColor = "#"+format( random.randint(0, COLORS_LIMIT), "X" ).zfill(COLOR_SIZE)
	constantColors.append( yearColor )
	
dataPreProcessing()
createDataFrames()
figureBar, loc = barTotalPerYear( "AGUASCALIENTES", YEAR, YEAR+N_YEARS )
figureLine, locs = lineAllYearsPerMonth( state = "AGUASCALIENTES", rows = 2, cols = 5 )

figureBar.savefig("Aguascalientes-ten-years-totals.png")
figureLine.savefig("Aguascalientes-ten-years-by-month.png")

checks = CheckButtons(buttonsArea, rainDictionaries.keys())
buttonsArea.set_title("Years")
checks.on_clicked( updateBarChart )

plt.show()
