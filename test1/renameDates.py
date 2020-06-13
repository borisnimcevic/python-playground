#! python3

import shutil, os, re

detePattern = re.compile(r"""^(.*?) #all text before the date
	((0|1)?\d)- #one or two digits fro the month
	((0|1|2|3)?\d)- #one or two digits for the day
	((19|20)\d\d)	#four digits for the year
	(.*?)$		#all text after the date
	""", re.VERBOSE)

#Loop over the files in the working directory
#Skip Files without a date
#Get the different parts of the filename
#From the European-style filename
#Get the full, absolute file paths.
#Rename the files
