import os.path
import json
import glob

dir=("C:\\PATH\\TO\\JSON\\FILES")
dirPattern=os.path.join(dir,'*.json')
fileList=glob.glob(dirQPattern)

while 1:
	q=input('"--ENTER SEARCH STRING-- :",\n ')

	for file in fileList:
		with open(file) as currFile:
			currText=json.load(currFile)
			if(q in currText["--//name to check in//--"]):
				print(currText["--//if name matches, print this value//-"])
