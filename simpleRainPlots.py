import matplotlib.pyplot as plt
from roundAlwaysUp import roundAlwaysUp
from matplotlib.widgets import RadioButtons

class SimpleRainPlots:

	def __init__(self, rainDictionaries):
		self.rainDictionaries = rainDictionaries
		
		defaultState = "AGUASCALIENTES"
		self.figure = plt.figure( constrained_layout=True )
		self.gridSpaceBarChart = self.figure.add_gridspec( 1, 6 ) 

		self.location = self.figure.add_subplot( self.gridSpaceBarChart[ 0, 1: ] ) 
		self.inputArea = self.figure.add_subplot( self.gridSpaceBarChart[ 0,0 ] )

		firstYear = list(self.rainDictionaries.keys())[0]
		self.AllStates = list(self.rainDictionaries[firstYear].keys())[0:-1]
		self.names = []
		for state in self.AllStates:
			self.names.append(state[0:3] + "." + state[-1])

		self.radio_buttons = RadioButtons(self.inputArea, tuple( self.names ) );
		self.buildInputArea()
		
		self.LineChartfigure, self.LineChartLocation = plt.subplots(2, 5, constrained_layout = True)
		

	def on_clicked(self, label):
		year = int( list( self.rainDictionaries.keys() )[0] )
		self.location.clear()
		
		self.barTotalPerYear(self.AllStates[ self.names.index(label) ], year, year + len( self.rainDictionaries.keys() ) )


		self.lineAllYearsPerMonth(self.AllStates[ self.names.index(label) ], 2, 5)
		plt.draw()

	#This function takes the state's name as argument and the range of years and creates and bar chart with the total precipitation per year.
	def barTotalPerYear(self, state, fromYear, toYear):
		ANUAL = "ANUAL"

		totals = {}

		for key,value in self.rainDictionaries.items():
			if int(key) >= fromYear and int(key) <= toYear:
				totals[key] = value[state][ANUAL]

		xPlaces = range( len( totals.keys() ) )
		
		self.location.bar( xPlaces, totals.values(), color = ["#00d9fe", "#2d96ff", "#4568d3"] )
		self.location.grid(True)

		self.location.set_axisbelow(True)
		self.location.set_xticks(xPlaces) 
		self.location.set_xticklabels(totals.keys(), fontsize=10)
		self.location.set_ylabel( "Valores en milimetros" )

		self.figure.suptitle("Precipitación anual en %s"% (state) )
		self.figure.canvas.set_window_title("Precipitación anual por estado de la república mexicana")
			
		return self.figure, self.location

	def setRainDictionaries(dictionaries):
		self.rainDictionaries = dictionaries
	
	def buildInputArea(self):
		self.radio_buttons.on_clicked( self.on_clicked)


	#A line graph of the state indicated, allocating every year we have as data in rows and cols indicated 
	def lineAllYearsPerMonth(self, state, rows, cols):
		X_INCHES_LAPTOP = 12
		Y_INCHES_LAPTOP = 7
		
		years = {}
		ROTATION_ANGLE = 90 #degrees

		for key, value in self.rainDictionaries.items():
			years[key] = value[state]
	
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
			self.LineChartLocation[r, c].clear()
			self.LineChartLocation[r, c].plot( months[0:-1], mm[0:-1] )# [0:] will get all the values but the last one which is the "ANUAL" value
			self.LineChartLocation[r, c].set_title( str(key) )
			self.LineChartLocation[r, c].grid(True)
			self.LineChartLocation[r, c].set_ylim(0, absoluteMax)
			self.LineChartLocation[r, c].set_yticks( self.LineChartLocation[r, c].get_yticks() )
			for label in self.LineChartLocation[r, c].get_xticklabels():
				label.set_rotation( ROTATION_ANGLE )

			c = c+1


		self.LineChartfigure.suptitle("Precipitación mensual en %s (%d años)" % (state, len ( self.rainDictionaries.items() ) ) )
		self.LineChartfigure.canvas.set_window_title("Precipitación mensual por estado de la república mexicana")
		self.LineChartfigure.set_size_inches(X_INCHES_LAPTOP + 1, X_INCHES_LAPTOP + 1)
		

		return self.LineChartfigure, self.LineChartLocation


