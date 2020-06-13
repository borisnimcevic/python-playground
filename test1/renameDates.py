#! python3

import shutil, os, re

detePattern = re.compile(r"""^(.*?) #all text before the date
	((0|1)?\d)- #one or two digits fro the month
	((0|1|2|3)?\d)- #one or two digits for the day
	((19|20)\d\d)	#four digits for the year
	(.*?)$		#all text after the date
	""", re.VERBOSE)

#Loop over the files in the working directory
for amerFilename in os.listdir('.'):
	mo = detePattern.search(amerFilename)

	if mo == None:
		continue

	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)
	#From the European-style filename
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	#Get the full, absolute file paths.
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)
	#Rename the files
	print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
	shutil.move(amerFilename, euroFilename) #uncoment after testing
