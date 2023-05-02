def readdata(range1,range2):
    data = open("Weather Report Project/data/19122.csv")
    dataTemp = []
    dataWindspeed = []
    windDir = []
    conditions = []

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
        countlines += 1

    return(dataTemp,dataWindspeed,windDir,conditions,countlines)
def clearAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "clear-day" or lines == "clear-night":
            count += 1
    output = (float(count/countlines))
    return output
def cloudyAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "cloudy":
            count += 1
    output = (float(count/countlines))
    return output
def partiallyCloudyAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "partly-cloudy-day" or lines == "partly-cloudy-night":
            count += 1
    output = (float(count/countlines))
    return output
def rainAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "rain":
            count += 1
    output = (float(count/countlines))
    return output
def snowAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "snow":
            count += 1
    output = (float(count/countlines))
    return output
def fogAllDay(conditions,countlines):
    count = 0
    for lines in conditions:
        if lines == "fog":
            count += 1
    output = (float(count/countlines))
    return output

def main ():
    range1 = 1
    range2 = 361

    readdata(range1,range2)
    dataTemp = readdata(range1,range2)[0]
    dataWindspeed = readdata(range1,range2)[1]
    windDir = readdata(range1,range2)[2]
    conditions = readdata(range1,range2)[3]
    countlines = readdata(range1,range2)[4]
    

    for i in conditions:
        print(i)
        pass
    #print(conditions,sep="\n")
    print("Amount lines:",countlines)
    print("rainAllDAy;",rainAllDay(conditions,countlines))
    print("snowAllDay",snowAllDay(conditions,countlines))
    print("fogAllDAy:",fogAllDay(conditions,countlines))
    print("clearAllDAy:",(clearAllDay(conditions,countlines)))
    print("cloudyAllDay:",(cloudyAllDay(conditions,countlines)))
    print("partallyCloudyAllDay:",(partiallyCloudyAllDay(conditions,countlines)))

    print("total",((partiallyCloudyAllDay(conditions,countlines))+(cloudyAllDay(conditions,countlines))+(clearAllDay(conditions,countlines))+((rainAllDay(conditions,countlines)))+(snowAllDay(conditions,countlines))+(fogAllDay(conditions,countlines))))
    
    print()
    print()


main()






def test1():
    data = open("Weather Report Project/data/19122.csv")
    text = data.read()
    #for line in text:
    #    text += "'"+line+"'"
    print(text)

#test1()
