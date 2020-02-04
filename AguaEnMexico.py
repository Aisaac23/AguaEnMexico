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

#mmExplained = "La precipitación pluvial se mide en mm, que sería el espesor de la lámina de agua que se formaría, a causa de la" +  " precipitación, sobre una superficie plana e impermeable y que equivale a litros de agua por metro cuadrado de terreno (l/m^2)."

rainDictionaries = {}

#Creating the paths to locate the .txt files and to create the .csv ones
for year in range(YEAR, YEAR+N_YEARS):
	txtPaths.append(PATH + str(year) + TXT_EXT)
	csvPaths.append(PATH + str(year) + CSV_EXT)
	
dataPreProcessing(txtPaths, csvPaths)
rainDictionaries = createDictionariesFromDataFrames(csvPaths, 2010)

simpPlots = SimpleRainPlots(rainDictionaries)

figureBar, loc = simpPlots.barTotalPerYear( "AGUASCALIENTES", YEAR, YEAR+N_YEARS )
figureLine, locs = simpPlots.lineAllYearsPerMonth( state = "AGUASCALIENTES", rows = 2, cols = 5 )

#figureBar.savefig("Aguascalientes-ten-years-totals.png")
#figureLine.savefig("Aguascalientes-ten-years-by-month.png")

interactiveRainP = InteractiveRainPlot(rainDictionaries)
interactiveRainP.buildSpaceForPlot()
interactiveRainP.buildButtonsArea()
interactiveRainP.barAllStatesAllYears(2010)

plt.show()
