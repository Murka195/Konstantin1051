def readdata(range1,range2,datei):
    data = open(datei)
    dataTemp = []
    dataWindspeed = []
    windDir = []
    conditions = []
    dateTime = []

    lines = data.readlines()

    countlines = 0
    for line in lines[range1:range2]:     #reads data into lists
       #print(line)
        quotecount = 0
        strings = []
        zwischenspeicher = ""
        '''
        for letter in line:
            if letter == '"':
                quotecount += 1
            # hier praktisch die ganze quote raus ignoreirern
            elif quotecount == 2 and letter == ",":
                # und hier nachdem es überspringen wrude
                quotecount = 0
                strings = line.split(",")
            elif quotecount != 1:
                strings = line.split(",")
        #'''
        for letter in line:
            #print(letter)
            if letter == '"':
                quotecount += 1
                zwischenspeicher += '"'
            # hier praktisch die ganze quote raus ignoreirern
            elif quotecount == 2 and letter == ",":
                # und hier nachdem es überspringen wrude
                quotecount = 0
                strings += [zwischenspeicher]
                zwischenspeicher = ""
            elif quotecount == 1:
                zwischenspeicher += letter
            elif letter == ",":
                #print(strings)
                strings += [zwischenspeicher]
                zwischenspeicher = ""
            else:
                zwischenspeicher += letter
        #print(strings)
        #'''

        #strings = line.split(",") 
        dataTemp.append(strings[2])
        dataWindspeed.append(strings[12])
        windDir.append(strings[13])
        conditions.append(strings[22])
        dateTime.append(strings[1])
        countlines += 1

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
    #while end != True:
        if clearAllDay2[0] > 0.9:
            return "It will be sunny all day."
        elif rainallDay2[0] > 0.9:
            return "It will be raining all day."
        elif snowAllDay2[0] > 0.9: 
            return "It will be snowing all day."
        elif fogAllDay2[0] > 0.9:
            return "It will be foggy all day."
        elif cloudyAllDay2[0] > 0.9:
            return "It will be cloudy all day."
        elif partiallyCloudyAllDay2[0] > 0.9:
            return "It will be partially cloudy all day."
        
        if (clearAllDay2[1] + clearAllDay2[2])/2 > 0.8:
            return "It will be sunny throuout the day. The night and evening might be different."
        elif (rainallDay2[1] + rainallDay2[2])/2 > 0.8:
            return "It will be raining throuout the day. The night and evening might be different."
        elif (snowAllDay2[1] + snowAllDay2[2])/2 > 0.8: 
            return "It will be snowing thouout the day. The night and evening might be different."
        elif (fogAllDay2[1] + fogAllDay2[2])/2 > 0.8:
            return "It will be foggy thouout the day. The night and evening might be different."
        elif (cloudyAllDay2[1] + cloudyAllDay2[2])/2 > 0.8:
            return "It will be cloudy thouout the day. The night and evening might be different."
        elif (partiallyCloudyAllDay2[0] + partiallyCloudyAllDay2[0])/2 > 0.9:
            return "It will be partially cloudy thouout the day. The night and evening might be different."
        
        else:
            return "Konstantin is stupid and this part of the program makes no sense."
        


        

        '''
            if clearAllDay2[1] > 0.9:
                return "The night will be clear."
            elif rainallDay2[1] > 0.9:
                return "It will be raining in the night."
            elif snowAllDay2[1] > 0.9: 
                return "It will snow in the night"
            elif fogAllDay2[1] > 0.9:
                return "The night will be foggy."
            elif cloudyAllDay2[1] > 0.9:
                return "It will be cloudy in the night"
            elif partiallyCloudyAllDay2[1] > 0.9:
                return "It will be partially clear in the night."
        
        '''

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
        added += int(i)
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


range1 = 0
def main (range1):
    datei = "Weather Report Project/data/19122 tomorrow4.csv"
    #range1 = 0
    range2 = range1+25

    readdata(range1,range2,datei)

    dataTemp = readdata(range1,range2,datei)[0]
    dataWindspeed = readdata(range1,range2,datei)[1]
    windDir = readdata(range1,range2,datei)[2]
    conditions = readdata(range1,range2,datei)[3]
    countlines = readdata(range1,range2,datei)[4]
    dateTime = readdata(range1,range2,datei)[5]
    
    #print(dateTime)
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
    date = dateTime[1]
    tomorowdate = ""
    #print(date)
    for i in range(10):
        tomorowdate += date[i]
    
    print("GÜÜD ËVBËNEENG.")
    print()
    print("The weather for -tomorow-",tomorowdate)
    print()
    print(answerOverallDay)
  
    tempMax = int(float(tempMaxMin(dataTemp)[1]))
    tempMin = int(float(tempMaxMin(dataTemp)[0]))
    print()
    print("The temperatures will be betwen",tempMin,"and",tempMax,"degrees celcius or between",(int(tempMin * 9/5) + 32),"and",(int(tempMax * 9/5) + 32),"degrees fahrenheit.")
    #print()
    #print(windMaxMin(dataWindspeed))
    print()
    averageWind = int((winddirection(windDir)))
    #print(averageWindInDirection(averageWind))
    
    print("The wind between 6am and 8pm will be comming from averaged",averageWind,"degrees or",averageWindInDirection(averageWind),"direction.")

    WindSpeedMax = int(float(tempMaxMin(dataWindspeed)[1]))
    WindSpeedMin = int(float(tempMaxMin(dataWindspeed)[0]))
    print()
    print("The windspeed will be between",WindSpeedMin,"and",WindSpeedMax,"kilometers per hour or beween",int(WindSpeedMin//1.609),"and",int(WindSpeedMax//1.609),"miles per hour.")

    
    
    
    print()


#rainallDay2,snowAllDay2,fogAllDay2,clearAllDay2,cloudyAllDay2,partiallyCloudyAllDay2










    #print()

def test1():
    data = open("Weather Report Project/data/19122.csv")
    text = data.read()
    #for line in text:
    #    text += "'"+line+"'"
    print(text)

main(range1)
#test1()


#main2 ()