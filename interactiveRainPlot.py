import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.widgets import CheckButtons
import matplotlib.patches as mpatches
from roundAlwaysUp import roundAlwaysUp

class InteractiveRainPlot:

	#Creates an "skeleton" for the chart to be drawn
	def __init__(self, rainDictionaries):
		self.rainDictionaries = rainDictionaries
		self.figure = plt.figure( constrained_layout=True )
		self.gridSpaceBarChart = self.figure.add_gridspec(3, 8)
		self.location = self.figure.add_subplot(self.gridSpaceBarChart[ : , 1: ]) 
		self.buttonsArea = self.figure.add_subplot(self.gridSpaceBarChart[0:2,0])
		self.checks = CheckButtons( self.buttonsArea, self.rainDictionaries.keys() ) 
		self.yearsDisplayed = []	
		self.constantColors = []
		self.COLORS_LIMIT = 16000000
		self.COLOR_SIZE = 6

	#Add details to the "skeleton"
	def buildSpaceForPlot(self):
		X_INCHES_LAPTOP = 12
		Y_INCHES_LAPTOP = 7

		self.figure.set_size_inches(X_INCHES_LAPTOP + 1, X_INCHES_LAPTOP + 1)
		self.figure.canvas.set_window_title("Precipitación anual de todos los estados de México (interactivo)")

		fillAx = self.figure.add_subplot( self.gridSpaceBarChart[2,0] )
		fillAx.set_axis_off()

	#Triggered every time we check or uncheck a checkbox
	def updateBarChart(self, label):
		self.location.cla()
		del( self.yearsDisplayed[:] )

		labels = self.checks.labels
		for index, checked in enumerate( self.checks.get_status() ):
			if checked:
				year_checked = labels[index].get_text()
				self.yearsDisplayed.append( year_checked )
		for year in self.yearsDisplayed:
			self.barAllStatesAllYears( int( year ) )

		plt.draw()

	#Add details to the buttons area and sets the function triggered to the corresponding event 
	def buildButtonsArea(self):
		self.buttonsArea.set_title("Years")
		self.checks.on_clicked( self.updateBarChart )
		for year in self.rainDictionaries.keys():
			yearColor = "#"+format( random.randint(0, self.COLORS_LIMIT), "X" ).zfill(self.COLOR_SIZE)
			self.constantColors.append( yearColor )
	
	def barAllStatesAllYears(self, year=2010):
		N_STATES = 32
		ROTATION_ANGLE = 45
		NACIONAL, ANUAL = "NACIONAL", "ANUAL"
		SHRINK_BAR = 0.11
		
		names = []
		both = [self.location, self.buttonsArea]
		colors = []

		states = {}
		totals = {}
		
		#If there is no year checked int the button area we add the default value or the one passed as argument.
		if( len(self.yearsDisplayed) == 0 ):
			self.yearsDisplayed.append(str(year));		

		states = self.rainDictionaries[year] # we get a dictionary with the form: {state:{month:amount}} for each year
		for state, value in states.items():
			if state != NACIONAL:
				totals[state] = value[ANUAL] # we get a dictionary with the form: {state:amount} for the "ANUAL" key
				colors.append( "#"+format( random.randint(0, self.COLORS_LIMIT), "X" ).zfill(self.COLOR_SIZE) )
			if len( names ) < N_STATES:
				names.append(state[0:3] + "." + state[-1])

		xPlaces = range( len( totals.keys() ) )
		
		absoluteMax = max( totals.values() )
		absoluteMax = roundAlwaysUp( absoluteMax )
		
		#Makes the rectangles to diferentiate each year in the legend.
		yearsRectangles = []
		shrinkTimes = 0
		if len( self.yearsDisplayed ) > 1:
			del( colors[:] )
			yLoc = 0
			for index, yd in enumerate( self.yearsDisplayed ):
				rect = mpatches.Rectangle( [yLoc, 0.001], 0.02, 0.02 )
				idColor = self.constantColors[index]
				if yd == str (year):
					colors = idColor
					shrinkTimes = index
				rect.set_color( idColor )
				yearsRectangles.append( rect )			
				yLoc = yLoc + 0.025
			

		allBars = self.location.bar( xPlaces, totals.values(), color = colors, edgecolor='black')#make a 32 colors scale
		
		for singleBar in allBars:
			singleBar.set_width( singleBar.get_width() - SHRINK_BAR*shrinkTimes )	

		self.location.grid(True)
		self.location.set_axisbelow(True)
		self.location.set_xticks(xPlaces) 

		self.location.set_xticklabels(names, fontsize=10)#pending
		self.location.set_ylabel( "Valores en milimetros" )
		self.location.set_ylim(0, absoluteMax)
		self.location.set_yticks( self.location.get_yticks() )
		
		self.location.legend(yearsRectangles, self.yearsDisplayed)
		
		formating = " - %s"*( len( self.yearsDisplayed )-1 )
		self.figure.suptitle( ( "Precipitación anual en %s" + ( formating ) )%  tuple( self.yearsDisplayed )  )

		for label in self.location.get_xticklabels():
			label.set_rotation( ROTATION_ANGLE )
		
		return self.figure, both
