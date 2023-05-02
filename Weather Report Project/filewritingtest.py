import csv

import requests
import sys

import codecs
        
response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/19122/tomorrow?unitGroup=metric&include=hours&key=7Z8KKMD3WEEF2ZYRNC25DVVRF&contentType=csv")
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  

CSVText = csv.reader(response.text.splitlines(), delimiter=',',quotechar='"')
        
datei = CSVText

dataTemp = []
dataWindspeed = []
windDir = []
conditions = []
dateTime = []
countlines = 25

for i in datei:
    dataTemp.append(i[2])
    dataWindspeed.append(i[12])
    windDir.append(i[13])
    conditions.append(i[22])
    dateTime.append(i[1])

print()

print(dataTemp,dataWindspeed,windDir,conditions,dateTime,sep= "\n\n")

output = str(dataTemp) + "\n\n" + str(dataWindspeed) + "\n\n" + str(windDir) + "\n\n" + str(conditions) + "\n\n" + str(dateTime)

#f = open("Weather Report Project/output", "w")
textfilename = dateTime[1]
with open('Weather Report Project/output/' + textfilename + ".txt",'w') as f:
    f.write(output)