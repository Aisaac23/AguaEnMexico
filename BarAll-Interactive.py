import pandas as pd
import matplotlib.pyplot as plt
from processCSVFilesFunctions import createDictionariesFromDataFrames
from interactiveRainPlot import InteractiveRainPlot


TXT_EXT, CSV_EXT = ".txt", ".csv"
YEAR, N_YEARS = 2010, 10
#PATH = "/home/isaac/Documentos/git/AguaEnMexico/Resumenes-Mensuales-de-precipitacion/"
txtPaths, csvPaths = [], []

PATH = input("Enter the full path where the monthly data is located: ")
YEAR = int( input("Enter the initial the initial year(1985-2020): ") )
N_YEARS = int( input("How many years from then will be analized? ") )

#mmExplained = "La precipitación pluvial se mide en mm, que sería el espesor de la lámina de agua que se formaría, a causa de la" +  " precipitación, sobre una superficie plana e impermeable y que equivale a litros de agua por metro cuadrado de terreno (l/m^2)."

rainDictionaries = {}

#Creating the paths to locate the .txt files and to create the .csv ones
for year in range(YEAR, YEAR+N_YEARS):
	txtPaths.append(PATH + str(year) + TXT_EXT)
	csvPaths.append(PATH + str(year) + CSV_EXT)
rainDictionaries = createDictionariesFromDataFrames(csvPaths, YEAR)

#Building the interactive plot
interactiveRainP = InteractiveRainPlot(rainDictionaries)
interactiveRainP.buildSpaceForPlot()
interactiveRainP.buildButtonsArea()
interactiveRainP.barAllStatesAllYears(YEAR)

plt.show()
