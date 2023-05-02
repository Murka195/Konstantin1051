    
def readdata(range1,datei):
    data = open(datei)
    dataTemp = []
    dataWindspeed = []
    windDir = []
    conditions = []
    dateTime = []

    lines = data.readlines()
    #print(lines)
    countlines = 0
    for line in lines[range1:25]:     #reads data into lists
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

    print(dataTemp,dataWindspeed,windDir,conditions,dateTime,sep= "\n\n")

range1 = 0
datei = "Weather Report Project/data/19122 tomorrow10.csv"

readdata(range1,datei)
