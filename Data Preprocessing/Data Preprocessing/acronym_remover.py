import numpy as npimport 
import csv
import re

def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        fileName = "C:\\Users\\HP\Desktop\\Machine Learning\\slang.txt"
        accessMode = "r"
        with open(fileName, accessMode) as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
            for row in dataFromFile:
                if _str.upper() == row[0]:
                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1
    final_string = ' '.join(user_string)
    return final_string

 def example():
 	ip = "WYD Send the work ASAP !"
	op = translator(ip)
	print("Input String - ")
	print()
	print(ip)
	print()
	print("Output String - ")
	print()
	print(op)