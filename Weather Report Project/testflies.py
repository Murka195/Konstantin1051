import csv

import requests
import sys

import codecs
        

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/19122/tomorrow?unitGroup=metric&include=hours&key=7Z8KKMD3WEEF2ZYRNC25DVVRF&contentType=csv")
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  


# Parse the results as CSV
CSVText = csv.reader(response.text.splitlines(), delimiter=',',quotechar='"')
        
datei = CSVText

'''
with open("Weather Report Project/data/19122 tomorrow10.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
'''
'''
feelslike = []
for line in CSVText:
    #feelslike += str(line[3])
    #print(line[3])
    feelslike.append(line[3])
    #feelslike += l
'''
'''
dataTemp.append(strings[2])
        dataWindspeed.append(strings[12])
        windDir.append(strings[13])
        conditions.append(strings[22])
        dateTime.append(strings[1])
'''

dataTemp = []
dataWindspeed = []
windDir = []
conditions = []
dateTime = []
countlines = 25

    #lines = data.readlines()
for i in datei:
    dataTemp.append(i[2])
    dataWindspeed.append(i[12])
    windDir.append(i[13])
    conditions.append(i[22])
    dateTime.append(i[1])
    #countlines += 1

print()

print(dataTemp,dataWindspeed,windDir,conditions,dateTime,sep= "\n\n")