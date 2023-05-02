def readdata(range1,range2):
    data = open("Weather Report Project/data/19122.csv")
    dataTemp = []
    dataWindspeed = []
    windDir = []
    conditions = []
    dateTime = []

    lines =  data.readlines()

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

def main ():
    range1 = 0
    range2 = range1+25

    readdata(range1,range2)

    dataTemp = readdata(range1,range2)[0]
    dataWindspeed = readdata(range1,range2)[1]
    windDir = readdata(range1,range2)[2]
    conditions = readdata(range1,range2)[3]
    countlines = readdata(range1,range2)[4]
    dateTime = readdata(range1,range2)[5]
    
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

    print("total all lines","\t",((partiallyCloudyAllDay(conditions,countlines)[0])+(cloudyAllDay(conditions,countlines)[0])+(clearAllDay(conditions,countlines)[0])+((rainAllDay(conditions,countlines))[0])+(snowAllDay(conditions,countlines)[0])+(fogAllDay(conditions,countlines)[0])))
    print("total0-5","\t\t",((partiallyCloudyAllDay(conditions,countlines)[1])+(cloudyAllDay(conditions,countlines)[1])+(clearAllDay(conditions,countlines)[1])+((rainAllDay(conditions,countlines))[1])+(snowAllDay(conditions,countlines)[1])+(fogAllDay(conditions,countlines)[1])))
    print("total6-11","\t\t",((partiallyCloudyAllDay(conditions,countlines)[2])+(cloudyAllDay(conditions,countlines)[2])+(clearAllDay(conditions,countlines)[2])+((rainAllDay(conditions,countlines))[2])+(snowAllDay(conditions,countlines)[2])+(fogAllDay(conditions,countlines)[2])))
    print("total12-17","\t\t",((partiallyCloudyAllDay(conditions,countlines)[3])+(cloudyAllDay(conditions,countlines)[3])+(clearAllDay(conditions,countlines)[3])+((rainAllDay(conditions,countlines))[3])+(snowAllDay(conditions,countlines)[3])+(fogAllDay(conditions,countlines)[3])))
    print("total18-23","\t\t",((partiallyCloudyAllDay(conditions,countlines)[4])+(cloudyAllDay(conditions,countlines)[4])+(clearAllDay(conditions,countlines)[4])+((rainAllDay(conditions,countlines))[4])+(snowAllDay(conditions,countlines)[4])+(fogAllDay(conditions,countlines)[4])))
    print("totalcount","\t\t",((partiallyCloudyAllDay(conditions,countlines)[5])+(cloudyAllDay(conditions,countlines)[5])+(clearAllDay(conditions,countlines)[5])+((rainAllDay(conditions,countlines))[5])+(snowAllDay(conditions,countlines)[5])+(fogAllDay(conditions,countlines)[5])))

    print()
    #print()

def test1():
    data = open("Weather Report Project/data/19122.csv")
    text = data.read()
    #for line in text:
    #    text += "'"+line+"'"
    print(text)

main()
#test1()


#main2 ()