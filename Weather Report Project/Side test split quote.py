#data = 'eine,keine,ich,muss,"eins,zwei,drei",deine,"vier,fünf",klaun'
#data = "19122,2023-03-14T00:00:00,4.7,1.3,2.4,84.88,0,0,rain"
data = '19122,2023-03-14T10:00:00,1.6,-4.4,-1.6,79.33,0.092,100,"rain,snow",0,'
zwischenspeicher = ""
quotecount = 0
strings = []

for letter in data:
    #strings = data.split(",")

    #'''
    
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
        strings += [zwischenspeicher]
        zwischenspeicher = ""
    else:
        zwischenspeicher += letter
#print(zwischenspeicher,quotecount)
#print(strings)

    #'''
print()
print(strings)
print()