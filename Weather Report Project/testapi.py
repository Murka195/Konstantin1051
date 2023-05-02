
import requests
import sys

import csv
import codecs
        

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/19122/tomorrow?unitGroup=metric&include=hours&key=7Z8KKMD3WEEF2ZYRNC25DVVRF&contentType=csv")
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  


# Parse the results as CSV
CSVText = csv.reader(response.text.splitlines(), delimiter=',',quotechar='"')

data = CSVText
'''
with open('eggs.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in spamreader:

        print(', '.join(row))



data = CSVText

lines =  data.readlines()

output = lines


with open('smallfriends.csv','rU') as csvfile:
readit = csv.reader(csvfile,delimiter=',')


for line in readit:
    print line

for line in readit:
    print 'foo'
'''

'''
#data = open('data.csv', 'r')
reader = csv.reader(data)

print(next(reader))               # Parse the first line
[next(data) for _ in range(5)]    # Skip the next 5 lines on the underlying iterator
print(next(reader))               # This will be the 7'th line in data
print(reader.line_num)            # reader thinks this is the 2nd line
data.seek(0)                      # Go back to the beginning of the file
print(next(reader))               # gives first line again

data = ['1,2,3', '4,5,6', '7,8,9']
reader = csv.reader(data)         # works fine on lists of strings too
print(next(reader))               # ['1', '2', '3']

'''
datei = CSVText

dataTemp = []
dataWindspeed = []
windDir = []
conditions = []
dateTime = []
countlines = 25

    #lines = data.readlines()
for i in datei:
    dataTemp = i[2]
    dataWindspeed = i[12]
    windDir = i[13]
    conditions = i[22]
    dateTime = i[1]
    #countlines += 1

for row in CSVText:
  print(row)
  print()

print(windDir)
print(dateTime)


print(CSVText)

#'''