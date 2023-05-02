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
def main(link):
    
    range1 = 0
    range2 = range1+25

    #readdata(range1,range2,datei)


    import csv

    import requests
    import sys
            
    #this code was taken from: https://www.visualcrossing.com/weather/weather-data-services# 
    
    response = requests.request("GET", link)
    if response.status_code!=200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()  


    # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',',quotechar='"')
            
    datei = CSVText

    dataTemp = []
    dataWindspeed = []
    windDir = []
    conditions = []
    dateTime = []
    location = []
    countlines = 25

    chartoutput =""

    #lines = data.readlines()
    for i in datei:
        dataTemp.append(i[2])
        dataWindspeed.append(i[12])
        windDir.append(i[13])
        conditions.append(i[22])
        dateTime.append(i[1])
        location.append(i[0])

    rainallDay2 = rainAllDay(conditions,countlines)
    snowAllDay2 = snowAllDay(conditions,countlines)
    fogAllDay2 = fogAllDay(conditions,countlines)
    clearAllDay2 = clearAllDay(conditions,countlines)
    cloudyAllDay2 = cloudyAllDay(conditions,countlines)
    partiallyCloudyAllDay2 = partiallyCloudyAllDay(conditions,countlines)


    print()
    chartoutput += "Amount lines:\t\t" + str(countlines) +"\n"
    chartoutput += "rainAllDAy:\t\t"+ str(rainallDay2) +"\n"
    chartoutput += "snowAllDay\t\t"+ str(snowAllDay2) + "\n"
    chartoutput += "fogAllDAy:\t\t"+ str(fogAllDay2) + "\n"
    chartoutput += "clearAllDAy:\t\t" + str(clearAllDay2) + "\n"
    chartoutput += "cloudyAllDay\t\t" + str(cloudyAllDay2)+ "\n"
    chartoutput += "partallyCloudyAllDay\t" + str(partiallyCloudyAllDay2) + "\n" + "\n"

    chartoutput += "total all lines\t\t"+   str(partiallyCloudyAllDay2[0]+cloudyAllDay2[0]+clearAllDay2[0]+rainallDay2[0]+snowAllDay2[0]+fogAllDay2[0]) + "\n"
    chartoutput += "total0-5\t\t"+          str(partiallyCloudyAllDay2[1]+cloudyAllDay2[1]+clearAllDay2[1]+rainallDay2[1]+snowAllDay2[1]+fogAllDay2[1])+ "\n"
    chartoutput += "total6-11\t\t"+         str(partiallyCloudyAllDay2[2]+cloudyAllDay2[2]+clearAllDay2[2]+rainallDay2[2]+snowAllDay2[2]+fogAllDay2[2])+ "\n"
    chartoutput += "total12-17\t\t"+        str(partiallyCloudyAllDay2[3]+cloudyAllDay2[3]+clearAllDay2[3]+rainallDay2[3]+snowAllDay2[3]+fogAllDay2[3])+ "\n"
    chartoutput += "total18-23\t\t"+        str(partiallyCloudyAllDay2[4]+cloudyAllDay2[4]+clearAllDay2[4]+rainallDay2[4]+snowAllDay2[4]+fogAllDay2[4])+ "\n"
    chartoutput += "totalcount\t\t"+        str(partiallyCloudyAllDay2[5]+cloudyAllDay2[5]+clearAllDay2[5]+rainallDay2[5]+snowAllDay2[5]+fogAllDay2[5])+ "\n"
   
    print()

    answerOverallDay = overallDay(rainallDay2,snowAllDay2,fogAllDay2,clearAllDay2,cloudyAllDay2,partiallyCloudyAllDay2)
    
    #text based report:
    date = dateTime[1]
    tomorowdate = ""
    #print(date)
    for i in range(10):
        tomorowdate += date[i]
    answer = ""
    answer += "Good Evening.\n\n"
    #print()
    answer += "The weather for " + str(tomorowdate) + " for " + str(location[1]) + "\n\n"
    #print()
    answer += answerOverallDay +"\n\n"
  
    tempMax = int(float(tempMaxMin(dataTemp)[1]))
    tempMin = int(float(tempMaxMin(dataTemp)[0]))
    #print()
    answer+= "The temperatures will be betwen "+str(tempMin)+" and "+str(tempMax)+" degrees celcius or between "+str((int(tempMin * 9/5) + 32))+" and "+str((int(tempMax * 9/5) + 32))+" degrees fahrenheit. \n\n"
    #print()
    #print(windMaxMin(dataWindspeed))
    #print()
    #print(windDir)
    averageWind = int((winddirection(windDir)))
    #averageWind = 0
    #print(averageWindInDirection(averageWind))
    
    answer += "The wind between 6am and 8pm will be comming from averaged "+str(averageWind)+" degrees or "+str(averageWindInDirection(averageWind))+" direction.\n\n"

    WindSpeedMax = int(float(tempMaxMin(dataWindspeed)[1]))
    WindSpeedMin = int(float(tempMaxMin(dataWindspeed)[0]))
    #print()
    answer += "The windspeed will be between "+str(WindSpeedMin)+" and "+str(WindSpeedMax) +" kilometers per hour or beween "+str(int(WindSpeedMin//1.609))+" and "+str(int(WindSpeedMax//1.609))+" miles per hour.\n\n"


    return answer,str(tomorowdate),str(location[1]),str(chartoutput)
    
    
    #print()
def showData(link):
    import csv

    import requests
    import sys

    import codecs
            

    response = requests.request("GET", link)
    if response.status_code!=200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()  


    # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',',quotechar='"')
            
    datei = CSVText

    dataTemp = []
    dataWindspeed = []
    windDir = []
    conditions = []
    dateTime = []#
    location = []
    countlines = 25

        #lines = data.readlines()
    for i in datei:
        dataTemp.append(i[2])
        dataWindspeed.append(i[12])
        windDir.append(i[13])
        conditions.append(i[22])
        dateTime.append(i[1])
        location.append(i[0])
        #countlines += 1

    print()

    print(dataTemp,dataWindspeed,windDir,conditions,dateTime,location,sep= "\n\n")

#postalCode = "18756 Greece"
#postalCode = "34711 USA" #ryan
postalCode = "24944 Germany"
#postalCode = "20740 USA"
#postalCode = "195271 Russia"
#postalCode = "SY8 2JQ England"
#postalCode = "SY3 7AA"

#postalCode = "19122 USA"

day = "today"

#link = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/19122/tomorrow?unitGroup=metric&include=hours&key=7Z8KKMD3WEEF2ZYRNC25DVVRF&contentType=csv"
link = ("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + postalCode + "/" + day + "?unitGroup=metric&include=hours&key=7Z8KKMD3WEEF2ZYRNC25DVVRF&contentType=csv")



output = (main(link))
print(output[3])
print(output[0])

textfilename = str(output[1])+" - "+ str(output[2])
with open('Weather Report Project/output/' + textfilename + ".txt",'w') as f:
    f.write(str(output[3] + "\n\n" + output[0]))
#showData(link)

'''
Was ich noch machen kann:
- Windrichtung in Halb richtungen einteilen
- Windrichtungen in Tageszeiten unterteilen






'''