import pandas as pd
import matplotlib.pyplot as plt
from dataPreProcessingFunctions import dataPreProcessing
from processCSVFilesFunctions import *

from simpleRainPlots import SimpleRainPlots
from interactiveRainPlot import InteractiveRainPlot


TXT_EXT, CSV_EXT = ".txt", ".csv"
YEAR, N_YEARS = 2010, 10
#PATH = "/home/isaac/Documentos/git/AguaEnMexico/Resumenes-Mensuales-de-precipitacion/"
txtPaths, csvPaths = [], []

PATH = input("Enter the full path where the monthly data is located: ")
#YEAR = int( input("Enter the initial the initial year: ") )
#N_YEARS = int( input("How many years from then will be analized? ") )

#mmExplained = "La precipitación pluvial se mide en mm, que sería el espesor de la lámina de agua que se formaría, a causa de la" +  " precipitación, sobre una superficie plana e impermeable y que equivale a litros de agua por metro cuadrado de terreno (l/m^2)."

rainDictionaries = {}

#Creating the paths to locate the .txt files and to create the .csv ones
for year in range(YEAR, YEAR+N_YEARS):
	txtPaths.append(PATH + str(year) + TXT_EXT)
	csvPaths.append(PATH + str(year) + CSV_EXT)

#getting the dictionaries from the dataFrames that were created with the CVS files.
rainDictionaries = createDictionariesFromDataFrames(csvPaths, 2010)

oneState = getAllYearsForState(csvPaths,'AGUASCALIENTES')

plt.show()
