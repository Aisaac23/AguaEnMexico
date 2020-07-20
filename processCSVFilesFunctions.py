import pandas as pd

def createDictionariesFromDataFrames(csvPaths, YEAR = 2010):
	ENTIDAD = "ENTIDAD"
	rainDataFrames = {}
	rainDictionaries = {}
	#creating a dictionary of dataframes with the years as keys (e.g 2010 -> dataframe_of_2010)
	for index, path in enumerate(csvPaths):
		rainDataFrames[index+YEAR] = pd.read_csv(path)

	#setting the column "ENTIDAD" as index of the dataframe since it'll be easier to iterate by name and all the names are unique.
	#also, we create a dictionary of dictionaries with the following format-> year:{"ENTIDAD":{"MONTH":amount}}
	for key, value in rainDataFrames.items():
		rainDictionaries[key] = value.set_index(ENTIDAD).to_dict("index")
	return rainDictionaries

def getAllYearsForState(csvPaths, entidad):
	ENTIDAD = "ENTIDAD"
	rainDataFrames = {}
	rainDictByMonth = {}
	rainDictionaries = {}
	#creating a dictionary of dataframes with the years as keys (e.g 2010 -> dataframe_of_2010)
	for index, path in enumerate(csvPaths):
		rainDataFrames[index+2010] = pd.read_csv(path)

	for key, value in rainDataFrames.items():
		rainDictionaries[key] = value.set_index(ENTIDAD).to_dict("index")

	for key, value in rainDictionaries.items():
		rainDictByMonth[key] = value[entidad].values
		print(rainDictByMonth[key]['ENE'])

	
	return rainDictByMonth
