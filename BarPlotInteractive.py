from processCSVFilesFunctions import createDictionariesFromDataFrames
from simpleRainPlots import SimpleRainPlots
import matplotlib.pyplot as plt

CSV_EXT = ".csv"
YEAR, N_YEARS = 2010, 10
PATH = input("Enter the full path where the monthly data is located: ")

csvPaths = []
rainDictionaries = {}

YEAR = int( input("Enter the initial the initial year(1985-2020): ") )
N_YEARS = int( input("How many years from then will be analized? ") )

#Creating the paths to locate the .txt files and to create the .csv ones
for year in range(YEAR, YEAR+N_YEARS):
	csvPaths.append(PATH + str(year) + CSV_EXT)


#getting the dictionaries from the dataFrames that were created with the CVS files.
rainDictionaries = createDictionariesFromDataFrames(csvPaths, YEAR)

#Creating an object for the simple plots and ploting the bar and the line chart of AGUASCALIENTES but could be of any other Mexico's sstate
simpPlots = SimpleRainPlots(rainDictionaries)
plt.show()

