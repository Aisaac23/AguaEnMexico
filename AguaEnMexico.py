import pandas as pd
import matplotlib.pyplot as plt
from dataPreProcessingFunctions import dataPreProcessing
from processCVSFilesFunctions import createDictionariesFromDataFrames
from simpleRainPlots import SimpleRainPlots
from interactiveRainPlot import InteractiveRainPlot

TXT_EXT, CSV_EXT = ".txt", ".csv"
YEAR, N_YEARS = 2010, 10
PATH = "/root/git/AguaEnMexico/Resumenes-Mensuales-de-precipitacion/"
txtPaths, csvPaths = [], []

PATH = input("Enter the full path where the monthly data is located: ")
YEAR = int( input("Enter the initial the initial year: ") )
N_YEARS = int( input("How many years from then will be analized? ") )

#mmExplained = "La precipitación pluvial se mide en mm, que sería el espesor de la lámina de agua que se formaría, a causa de la" +  " precipitación, sobre una superficie plana e impermeable y que equivale a litros de agua por metro cuadrado de terreno (l/m^2)."

rainDictionaries = {}

#Creating the paths to locate the .txt files and to create the .csv ones
for year in range(YEAR, YEAR+N_YEARS):
	txtPaths.append(PATH + str(year) + TXT_EXT)
	csvPaths.append(PATH + str(year) + CSV_EXT)

#executing the dataPreProcessing module
dataPreProcessing(txtPaths, csvPaths)

#getting the dictionaries from the dataFrames that were created with the CVS files.
rainDictionaries = createDictionariesFromDataFrames(csvPaths, 2010)

#Creating an object for the simple plots
simpPlots = SimpleRainPlots(rainDictionaries)

STATE = input("Enter the name of a Mexico's state to get its yearly data: ")

#Ploting the bar and the line chart of AGUASCALIENTES but could be of any other Mexico's sstate
figureBar, loc = simpPlots.barTotalPerYear( STATE.upper(), YEAR, YEAR+N_YEARS )

STATE = input("Enter the name of a Mexico's state to get its monthly data over the total of years: ")

figureLine, locs = simpPlots.lineAllYearsPerMonth( STATE.upper(), rows = 2, cols = 5 )

#Building the interactive plot
interactiveRainP = InteractiveRainPlot(rainDictionaries)
interactiveRainP.buildSpaceForPlot()
interactiveRainP.buildButtonsArea()
interactiveRainP.barAllStatesAllYears(2010)

plt.show()
