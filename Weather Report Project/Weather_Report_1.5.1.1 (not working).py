def readdata(range1,range2,datei):
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

    return(dataTemp,dataWindspeed,windDir,conditions,countlines,dateTime)
def clearAllDay(conditions,countlines):

    count = 0
    for lines in conditions:
        if lines == "clear-day" or lines == "clear-night":
            count += 1
    ratio = (float(count/countlines))
    #night 0-6 Uhr


    countN= 0
    for lines in conditions[1:7]:
        if lines == "clear-day" or lines == "clear-night":
            countN += 1
    ratioN = (float(countN/6))


    countM= 0
    for lines in conditions[7:13]:
        if lines == "clear-day" or lines == "clear-night":
            countM += 1
    ratioM = (float(countM/6))

    countAN= 0
    for lines in conditions[13:19]:
        if lines == "clear-day" or lines == "clear-night":
            countAN += 1
    ratioAN = (float(countAN/6))

    countE= 0
    for lines in conditions[19:25]:
        if lines == "clear-day" or lines == "clear-night":
            countE += 1
    ratioE = (float(countE/6))

    return (ratio,ratioN,ratioM,ratioAN,ratioE,count)



    '''
    for i in range[dateTime[11:12]:dateTime[11+1]]:
        
        # war gerade hier am arbeiten wie ich eine zeitlich abhängikeit für die zeiten einbauen kann
        pass
        # ich lasse das erstmal so, als gehe ich davon aus, dass es nur ein Tag ist
        > müsste man hier ändern


    '''



    #if ratio != 
def cloudyAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "cloudy":
            count += 1
    ratio = (float(count/countlines))

    countN= 0
    for lines in conditions[1:7]:
        if lines == "cloudy":
            countN += 1
    ratioN = (float(countN/6))


    countM= 0
    for lines in conditions[7:13]:
        if lines == "cloudy":
            countM += 1
    ratioM = (float(countM/6))

    countAN= 0
    for lines in conditions[13:19]:
        if lines == "cloudy":
            countAN += 1
    ratioAN = (float(countAN/6))

    countE= 0
    for lines in conditions[19:25]:
        if lines == "cloudy":
            countE += 1
    ratioE = (float(countE/6))

    return (ratio,ratioN,ratioM,ratioAN,ratioE,count)

def partiallyCloudyAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "partly-cloudy-day" or lines == "partly-cloudy-night":
            count += 1
    ratio = (float(count/countlines))

    countN= 0
    for lines in conditions[1:7]:
        if lines == "partly-cloudy-day" or lines == "partly-cloudy-night":
            countN += 1
    ratioN = (float(countN/6))


    countM= 0
    for lines in conditions[7:13]:
        if lines == "partly-cloudy-day" or lines == "partly-cloudy-night":
            countM += 1
    ratioM = (float(countM/6))

    countAN= 0
    for lines in conditions[13:19]:
        if lines == "partly-cloudy-day" or lines == "partly-cloudy-night":
            countAN += 1
    ratioAN = (float(countAN/6))

    countE= 0
    for lines in conditions[19:25]:
        if lines == "partly-cloudy-day" or lines == "partly-cloudy-night":
            countE += 1
    ratioE = (float(countE/6))

    return (ratio,ratioN,ratioM,ratioAN,ratioE,count) 

def rainAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "rain":
            count += 1
    ratio = (float(count/countlines))

    countN= 0
    for lines in conditions[1:7]:
        if lines == "rain":
            countN += 1
    ratioN = (float(countN/6))


    countM= 0
    for lines in conditions[7:13]:
        if lines == "rain":
            countM += 1
    ratioM = (float(countM/6))

    countAN= 0
    for lines in conditions[13:19]:
        if lines == "rain":
            countAN += 1
    ratioAN = (float(countAN/6))

    countE= 0
    for lines in conditions[19:25]:
        if lines == "rain":
            countE += 1
    ratioE = (float(countE/6))

    return (ratio,ratioN,ratioM,ratioAN,ratioE,count) 

def snowAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "snow":
            count += 1
    ratio = (float(count/countlines))

    
    countN= 0
    for lines in conditions[1:7]:
        if lines == "snow":
            countN += 1
    ratioN = (float(countN/6))


    countM= 0
    for lines in conditions[7:13]:
        if lines == "snow":
            countM += 1
    ratioM = (float(countM/6))

    countAN= 0
    for lines in conditions[13:19]:
        if lines == "snow":
            countAN += 1
    ratioAN = (float(countAN/6))

    countE= 0
    for lines in conditions[19:25]:
        if lines == "snow":
            countE += 1
    ratioE = (float(countE/6))

    return (ratio,ratioN,ratioM,ratioAN,ratioE,count) 

def fogAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "fog":
            count += 1
    ratio = (float(count/countlines))
    countN= 0
    for lines in conditions[1:7]:
        if lines == "fog":
            countN += 1
    ratioN = (float(countN/6))


    countM= 0
    for lines in conditions[7:13]:
        if lines == "fog":
            countM += 1
    ratioM = (float(countM/6))

    countAN= 0
    for lines in conditions[13:19]:
        if lines == "fog":
            countAN += 1
    ratioAN = (float(countAN/6))

    countE= 0
    for lines in conditions[19:25]:
        if lines == "fog":
            countE += 1
    ratioE = (float(countE/6))

    return (ratio,ratioN,ratioM,ratioAN,ratioE,count) 

def overallDay(rainallDay2,snowAllDay2,fogAllDay2,clearAllDay2,cloudyAllDay2,partiallyCloudyAllDay2):
    #end = False
    for i in range (1): #> 90%
        output = ""
        if fogAllDay2[0] > 0.9:
            output += "It will be foggy all day. "
            if snowAllDay2[0]  > 0.0:
                output += "There might also be some snow. "
            if rainallDay2[0]  > 0.0:
                output += "There might also be some rain. "
            if fogAllDay2[0]  > 0.0:
                output += "There might also be some fog. "

        elif snowAllDay2[0] > 0.9: 
            output += "It will be snowing all day. "
            if rainallDay2[0]  > 0.0:
                output += "There might also be some rain. "
            if fogAllDay2[0]  > 0.0:
                output += "There might also be some fog. "

        elif rainallDay2[0] > 0.9:
            output += "It will be raining all day. "
            if snowAllDay2[0]  > 0.0:
                output += "There might also be some snow. "
            if fogAllDay2[0]  > 0.0:
                output += "There might also be some fog. "
        
        elif cloudyAllDay2[0] > 0.9:
            output += "It will be cloudy all day. "
            if rainallDay2[0]  > 0.0:
                output += ". There might also be some rain. "
            else:
                output += ", but there will be no rain. "
            if fogAllDay2[0]  > 0.0:
                output += "There might be some fog. "


        elif partiallyCloudyAllDay2[0] > 0.9:
            output += "It will be partially cloudy all day"
            if rainallDay2[0]  > 0.0:
                output += ". There might also be some rain. "
            else:
                output += ". "
            if fogAllDay2[0]  > 0.0:
                output += "There might be some fog. "

        elif clearAllDay2[0] > 0.9:
            output += "It will be sunny all day"
            if rainallDay2[0] > 0.0:
                output += ", but there might be some rain"
            else:
                output += ". " 
            if fogAllDay2[0]  > 0.0:
                output += "There might also be some fog. "
  
    for i in range (1): #> 50%
        if output == "":
            output += "The weather will be changing. \n"
    
            
            if (cloudyAllDay2[1] + partiallyCloudyAllDay2[1])/2 > 0.8:
                output += "There will be clouds the whole night. \n"
            elif (cloudyAllDay2[1] + partiallyCloudyAllDay2[1])/2 > 0.5:
                output += "There will be partly clouds in the night. \n"
            elif (cloudyAllDay2[1] + partiallyCloudyAllDay2[1])/2 > 0.0:
                output += "There will be some clouds in the night. \n"

            if (cloudyAllDay2[2] + partiallyCloudyAllDay2[2])/2 > 0.8:
                output += "There will be clouds the whole morning. \n"
            elif (cloudyAllDay2[2] + partiallyCloudyAllDay2[2])/2 > 0.5:
                output += "There will be partly clouds in the morning. \n"
            elif (cloudyAllDay2[2] + partiallyCloudyAllDay2[2])/2 > 0.0:
                output += "There will be some clouds in the morning. \n"
            
            if (cloudyAllDay2[3] + partiallyCloudyAllDay2[3])/2 > 0.8:
                output += "There will be clouds the whole afternoon. \n"
            elif (cloudyAllDay2[3] + partiallyCloudyAllDay2[3])/2 > 0.5:
                output += "There will be partly clouds in the afternoon. \n"
            elif (cloudyAllDay2[3] + partiallyCloudyAllDay2[3])/2 > 0.0:
                output += "There will be some clouds in the afternoon. \n"

            if (cloudyAllDay2[4] + partiallyCloudyAllDay2[4])/2 > 0.8:
                output += "There will be clouds the whole evening. \n"
            elif (cloudyAllDay2[4] + partiallyCloudyAllDay2[4])/2 > 0.5:
                output += "There will be partly clouds in the evening. \n"
            elif (cloudyAllDay2[4] + partiallyCloudyAllDay2[4])/2 > 0.0:
                output += "There will be some clouds in the evening. \n"

            #partly cloudy erstmal ausgelassen


            if rainallDay2[1] > 0.8:
                output += "It will be raining the whole night. \n"
            elif rainallDay2[1] > 0.5:
                output += "It will be partly raining in the night. \n"
            elif rainallDay2[1] > 0.0:
                output += "It will be some raining in the night. \n"

            if rainallDay2[2] > 0.8:
                output += "It will be raining the whole morning. \n"
            elif rainallDay2[2] > 0.5:
                output += "It will be partly raining in the morning. \n"
            elif rainallDay2[2] > 0.0:
                output += "It will be some raining in the morning. \n"
            
            if rainallDay2[3] > 0.8:
                output += "It will be raining the whole afternoon. \n"
            elif rainallDay2[3] > 0.5:
                output += "It will be partly raining in the afternoon. \n"
            elif rainallDay2[3] > 0.0:
                output += "It will be some raining in the afternoon. \n"

            if rainallDay2[4] > 0.8:
                output += "It will be raining the whole evening. \n"
            elif rainallDay2[4] > 0.5:
                output += "It will be partly raining in the evening. \n"
            elif rainallDay2[4] > 0.0:
                output += "It will be some raining in the evening. \n"
            
            if fogAllDay2[1] > 0.8:
                output += "It will be foggy the whole night. \n"
            elif fogAllDay2[1] > 0.5:
                output += "It will be partly foggy in the night. \n"
            elif fogAllDay2[1] > 0.0:
                output += "It will be some foggy in the night. \n"

            if fogAllDay2[2] > 0.8:
                output += "It will be foggy the whole morning. \n"
            elif fogAllDay2[2] > 0.5:
                output += "It will be partly foggy in the morning. \n"
            elif fogAllDay2[2] > 0.0:
                output += "It will be some foggy in the morning. \n"
            
            if fogAllDay2[3] > 0.8:
                output += "It will be foggy the whole afternoon. \n"
            elif fogAllDay2[3] > 0.5:
                output += "It will be partly foggy in the afternoon. \n"
            elif fogAllDay2[3] > 0.0:
                output += "It will be some foggy in the afternoon. \n"

            if fogAllDay2[4] > 0.8:
                output += "It will be foggy the whole evening. \n"
            elif fogAllDay2[4] > 0.5:
                output += "It will be partly foggy in the evening. \n"
            elif fogAllDay2[4] > 0.0:
                output += "It will be some foggy in the evening. \n"


            
            if snowAllDay2[1] > 0.8:
                output += "It will be snowy the whole night. \n"
            elif snowAllDay2[1] > 0.5:
                output += "It will be partly snowy in the night. \n"
            elif snowAllDay2[1] > 0.0:
                output += "It will be some snowy in the night. \n"

            if snowAllDay2[2] > 0.8:
                output += "It will be snowy the whole morning. \n"
            elif snowAllDay2[2] > 0.5:
                output += "It will be partly snowy in the morning. \n"
            elif snowAllDay2[2] > 0.0:
                output += "It will be some snowy in the morning. \n"
            
            if snowAllDay2[3] > 0.8:
                output += "It will be snowy the whole afternoon. \n"
            elif snowAllDay2[3] > 0.5:
                output += "It will be partly snowy in the afternoon. \n"
            elif snowAllDay2[3] > 0.0:
                output += "It will be some snowy in the afternoon. \n"

            if snowAllDay2[4] > 0.8:
                output += "It will be snowy the whole evening. \n"
            elif snowAllDay2[4] > 0.5:
                output += "It will be partly snowy in the evening. \n"
            elif snowAllDay2[4] > 0.0:
                output += "It will be some snowy in the evening. \n"

            if clearAllDay2[1] > 0.8:
                output += "It will be clear the whole night. \n"
            elif clearAllDay2[1] > 0.5:
                output += "It will be partly clear in the night. \n"
            elif clearAllDay2[1] > 0.0:
                output += "It will be some clear in the night. \n"

            if clearAllDay2[2] > 0.8:
                output += "It will be clear the whole morning. \n"
            elif clearAllDay2[2] > 0.5:
                output += "It will be partly clear in the morning. \n"
            elif clearAllDay2[2] > 0.0:
                output += "It will be some clear in the morning. \n"
            
            if clearAllDay2[3] > 0.8:
                output += "It will be clear the whole afternoon. \n"
            elif clearAllDay2[3] > 0.5:
                output += "It will be partly clear in the afternoon. \n"
            elif clearAllDay2[3] > 0.0:
                output += "It will be some clear in the afternoon. \n"

            if clearAllDay2[4] > 0.8:
                output += "It will be clear the whole evening. \n"
            elif clearAllDay2[4] > 0.5:
                output += "It will be partly clear in the evening. \n"
            elif clearAllDay2[4] > 0.0:
                output += "It will be some clear in the evening. \n"
    
    
    return output
        

def tempMaxMin(dataTemp):
    maxTemp = -999999
    minTemp = 999999
    #'''
    for value in dataTemp[2:]:
        #print(value)
        if float(value) > float(maxTemp):
            maxTemp = value
    #'''
    #'''        
    for value in dataTemp[2:]:
        #print(value)
        if float(value) < float(minTemp):
            minTemp = value
    return minTemp,maxTemp
    #'''
    
def windMaxMin(dataWindspeed):
    maxWindSpeed = -999999
    minWindSpeed = 999999
    #'''
    for value in dataWindspeed[2:]:
        #print(value)
        if float(value) > float(maxWindSpeed):
            maxWindSpeed = value
    #'''
    #'''        
    for value in dataWindspeed[2:]:
        #print(value)
        if float(value) < float(minWindSpeed):
            minWindSpeed = value
    return minWindSpeed,maxWindSpeed
    
def winddirection(windDir):
    #average between 6 and 20 Uhr
    added = 0
    count = 0
    for i in windDir[7:21]:
        added += int(float((i)))
        count += 1
        #print(i)
    return (added/count)

def averageWindInDirection(averageWind):
    if 314 < averageWind < 361 or -1 < averageWind < 46:
        #return "The wind will come from",averageWind,"or north direction."
        return "north"
    elif 45 < averageWind < 136:
        #return "The wind will come from",averageWind,"or east direction."
        return "east"
    elif 135 < averageWind < 236:
        #return "The wind will come from",averageWind,"or south direction."
        return "south"
    elif 235 < averageWind < 315:
        #return "The wind will come from",averageWind,"or west direction."
        return "west"
    else:
        return "Something is messed up with the wind direction."

def main (datei):
    
    range1 = 0
    range2 = range1+25

    readdata(range1,range2,datei)

    dataTemp = readdata(range1,range2,datei)[0]
    dataWindspeed = readdata(range1,range2,datei)[1]
    windDir = readdata(range1,range2,datei)[2]
    conditions = readdata(range1,range2,datei)[3]
    countlines = readdata(range1,range2,datei)[4]
    dateTime = readdata(range1,range2,datei)[5]
    
    print(dateTime)
    '''
    for i in dateTime:
        print(i)
        #pass
    '''

    #print(conditions,sep="\n")
    print()
    print("Amount lines:","\t\t",countlines)
    print("rainAllDAy;","\t\t",rainAllDay(conditions,countlines))
    print("snowAllDay","\t\t",snowAllDay(conditions,countlines))
    print("fogAllDAy:","\t\t",fogAllDay(conditions,countlines))
    print("clearAllDAy:","\t\t",(clearAllDay(conditions,countlines)))
    print("cloudyAllDay:","\t\t",(cloudyAllDay(conditions,countlines)))
    print("partallyCloudyAllDay:","\t",(partiallyCloudyAllDay(conditions,countlines)))

    rainallDay2 = rainAllDay(conditions,countlines)
    snowAllDay2 = snowAllDay(conditions,countlines)
    fogAllDay2 = fogAllDay(conditions,countlines)
    clearAllDay2 = clearAllDay(conditions,countlines)
    cloudyAllDay2 = cloudyAllDay(conditions,countlines)
    partiallyCloudyAllDay2 = partiallyCloudyAllDay(conditions,countlines)




    #hier kann man noch austauschen um einfacher zu machen

    print("total all lines","\t",((partiallyCloudyAllDay(conditions,countlines)[0])+(cloudyAllDay(conditions,countlines)[0])+(clearAllDay(conditions,countlines)[0])+((rainAllDay(conditions,countlines))[0])+(snowAllDay(conditions,countlines)[0])+(fogAllDay(conditions,countlines)[0])))
    print("total0-5","\t\t",((partiallyCloudyAllDay(conditions,countlines)[1])+(cloudyAllDay(conditions,countlines)[1])+(clearAllDay(conditions,countlines)[1])+((rainAllDay(conditions,countlines))[1])+(snowAllDay(conditions,countlines)[1])+(fogAllDay(conditions,countlines)[1])))
    print("total6-11","\t\t",((partiallyCloudyAllDay(conditions,countlines)[2])+(cloudyAllDay(conditions,countlines)[2])+(clearAllDay(conditions,countlines)[2])+((rainAllDay(conditions,countlines))[2])+(snowAllDay(conditions,countlines)[2])+(fogAllDay(conditions,countlines)[2])))
    print("total12-17","\t\t",((partiallyCloudyAllDay(conditions,countlines)[3])+(cloudyAllDay(conditions,countlines)[3])+(clearAllDay(conditions,countlines)[3])+((rainAllDay(conditions,countlines))[3])+(snowAllDay(conditions,countlines)[3])+(fogAllDay(conditions,countlines)[3])))
    print("total18-23","\t\t",((partiallyCloudyAllDay(conditions,countlines)[4])+(cloudyAllDay(conditions,countlines)[4])+(clearAllDay(conditions,countlines)[4])+((rainAllDay(conditions,countlines))[4])+(snowAllDay(conditions,countlines)[4])+(fogAllDay(conditions,countlines)[4])))
    print("totalcount","\t\t",((partiallyCloudyAllDay(conditions,countlines)[5])+(cloudyAllDay(conditions,countlines)[5])+(clearAllDay(conditions,countlines)[5])+((rainAllDay(conditions,countlines))[5])+(snowAllDay(conditions,countlines)[5])+(fogAllDay(conditions,countlines)[5])))

    print()

    answerOverallDay = overallDay(rainallDay2,snowAllDay2,fogAllDay2,clearAllDay2,cloudyAllDay2,partiallyCloudyAllDay2)
    
    #text based report:
    #print(dataTemp[1])
    #date = dateTime[1]
    #date = "28mal"
    tomorowdate = ""
    #print(date)
    #for i in range(10):
     #   tomorowdate += date[i]
    
    print("GÜÜD ËVBËNEENG.")
    print()
    print("The weather for -tomorow-",tomorowdate)
    print()
    print(answerOverallDay)
  
    tempMax = int(float(tempMaxMin(dataTemp)[1]))
    tempMin = int(float(tempMaxMin(dataTemp)[0]))
    #print()
    print("The temperatures will be betwen",tempMin,"and",tempMax,"degrees celcius or between",(int(tempMin * 9/5) + 32),"and",(int(tempMax * 9/5) + 32),"degrees fahrenheit.")
    #print()
    #print(windMaxMin(dataWindspeed))
    print()
    #print(windDir)
    averageWind = int((winddirection(windDir)))
    #averageWind = 0
    #print(averageWindInDirection(averageWind))
    
    print("The wind between 6am and 8pm will be comming from averaged",averageWind,"degrees or",averageWindInDirection(averageWind),"direction.")

    WindSpeedMax = int(float(tempMaxMin(dataWindspeed)[1]))
    WindSpeedMin = int(float(tempMaxMin(dataWindspeed)[0]))
    print()
    print("The windspeed will be between",WindSpeedMin,"and",WindSpeedMax,"kilometers per hour or beween",int(WindSpeedMin//1.609),"and",int(WindSpeedMax//1.609),"miles per hour.")

    
    
    
    print()
range1 = 0

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
        
datei = CSVText

#datei = "Weather Report Project/data/19122 tomorrow8.csv"
#datei = 
main(datei)

#rainallDay2,snowAllDay2,fogAllDay2,clearAllDay2,cloudyAllDay2,partiallyCloudyAllDay2
    #print()

def test1():
    data = open("Weather Report Project/data/19122.csv")
    text = data.read()
    #for line in text:
    #    text += "'"+line+"'"
    print(text)

#test1()
#main2 ()



#old code
'''


            elif snowAllDay2[0] > 0.9: 
                output += "It will be snowing all day. "
                if rainallDay2[0]  > 0.0:
                    output += "There might also be some rain. "


                if (snowAllDay2[1] + snowAllDay2[2] + snowAllDay2[3] + snowAllDay2[4])/4 > 0.3:
                        output+= "It will snow throughout the whole day. "

                elif (snowAllDay2[2] + snowAllDay2[3])/2 > 0.3:
                    output += "It will snow primarily throught daytime. "
                    #if snowAllDay2

                elif (snowAllDay2[1] + snowAllDay2[4])/2 > 0.3:
                    output += "It will snow primarily throught the night. "

                elif snowAllDay2[2] > 0.3:
                    output += "It will snow primarily in the morning "
                    if snowAllDay2[3] > 0.0:
                        output += "But there will be also snow in the afternoon. "
                
                elif snowAllDay2[3] > 0.3:
                    answer = ""
                    if snowAllDay2[1] > 0.0:
                        output+= "There will be some snow in the night. "
                        answer == "also"
                    if snowAllDay2[2] > 0.0:
                        output += "There will",answer, "be some snow in the morning, but mostly in the afternoon"
                    else:
                        output += "It will",answer,"snow primarily in the afternoon "







            #elif rainallDay2[0] > 0.5:
                output += "It will be primarily raining > 0.5 throughout the day. "
                
            
                
    
    
                if snowAllDay2[1]  > 0.3:
                    output += "It will be snowy especially in the night. "
                if rainallDay2[1]  > 0.3:
                    output += "There will also be some rain in the night. "
                
                if snowAllDay2[0]  > 0.0:
                    output += "There might also be some snow. "
                if rainallDay2[0]  > 0.0:
                    output += "There might also be some rain. "

                
            
            elif cloudyAllDay2[0] > 0.9:
                output += "It will be cloudy all day. "
                if rainallDay2[0]  > 0.0:
                    output += ". There might also be some rain. "
                else:
                    output += ", but there will be no rain. "
            elif partiallyCloudyAllDay2[0] > 0.9:
                output += "It will be partially cloudy all day"
                if rainallDay2[0]  > 0.0:
                    output += ". There might also be some rain. "
                else:
                    output += ". "

            elif clearAllDay2[0] > 0.9:
                output += "It will be sunny all day"
                if rainallDay2[0] > 0.0:
                    output += ", but there might be some rain"
                else:
                    output += ". "



'''