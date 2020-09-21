import matplotlib.pyplot as plt
import matplotlib.patches as ptchs
from roundAlwaysUp import roundAlwaysUp
from matplotlib.widgets import RadioButtons

class SimpleRainPlots:

	def __init__(self, rainDictionaries):
		self.rainDictionaries = rainDictionaries
		
		self.figure = plt.figure( constrained_layout=True )
		self.gridSpaceBarChart = self.figure.add_gridspec( 1, 6 )
		

		self.location = self.figure.add_subplot( self.gridSpaceBarChart[ 0, 2: ] ) 
		self.inputArea = self.figure.add_subplot( self.gridSpaceBarChart[ 0,0:2 ] )

		firstYear = list(self.rainDictionaries.keys())[0]
		self.AllStates = list(self.rainDictionaries[firstYear].keys())[0:-1]
		self.names = []
		for state in self.AllStates:
			self.names.append(state)

		
		self.radio_buttons = RadioButtons(self.inputArea, tuple( self.names ) , active=0);
		self.buildInputArea()
		self.inputArea.set_facecolor( 'lightgoldenrodyellow' )
		self.barTotalPerYear(self.names[0], firstYear, firstYear + len( self.rainDictionaries.keys() ) )

	def on_clicked(self, label):
		year = int( list( self.rainDictionaries.keys() )[0] )
		self.location.clear()
		
		self.barTotalPerYear(self.AllStates[ self.names.index(label) ], year, year + len( self.rainDictionaries.keys() ) )

		plt.draw()

	#This function takes the state's name as argument and the range of years and creates and bar chart with the total precipitation per year.
	def barTotalPerYear(self, state, fromYear, toYear):
		ANUAL = "ANUAL"
		X_INCHES_LAPTOP = 12
		Y_INCHES_LAPTOP = 7

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

