import sys




txt_file = sys.argv[1]

rain_file = open( txt_file )
lines = rain_file.readlines()

output = []

for line in lines:
	words = line.split()
	output = [word for word in words if word.isalpha()]

for word in output:
	print(word)

