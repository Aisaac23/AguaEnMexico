import matplotlib.pyplot as plt
from roundAlwaysUp import roundAlwaysUp

class SimpleRainPlots:

	def __init__(self, rainDictionaries):
		self.rainDictionaries = rainDictionaries

	#This function takes the state's name as argument and the range of years and creates and bar chart with the total precipitation per year.
	def barTotalPerYear(self, state, fromYear, toYear):
		ANUAL = "ANUAL"

		totals = {}
		figure, location = plt.subplots(1, 1)

		for key,value in self.rainDictionaries.items():
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

	def setRainDictionaries(dictionaries):
		rainDictionaries = dictionaries

	#A line graph of the state indicated, allocating every year we have as data in rows and cols indicated 
	def lineAllYearsPerMonth(self, state, rows, cols):
		X_INCHES_LAPTOP = 12
		Y_INCHES_LAPTOP = 7
		
		years = {}
		ROTATION_ANGLE = 90 #degrees

		for key, value in self.rainDictionaries.items():
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


		figure.suptitle("Precipitación mensual en %s (%d años)" % (state, len ( self.rainDictionaries.items() ) ) )
		figure.canvas.set_window_title("Precipitación mensual por estado de la república mexicana")
		figure.set_size_inches(X_INCHES_LAPTOP + 1, X_INCHES_LAPTOP + 1)
		return figure, location


