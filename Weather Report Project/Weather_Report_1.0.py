#data = open("Weather Report Project/data/19122 tomorrow.csv")
data = open("Weather Report Project/data/19122.csv")
#data = open("/Users/konstantin/Documents/00 Privat/Studium/Unterricht /Semester 2/CIS 1051/Code Visual II/Weather Report Project/data/19122 tomorrow.csv")


dataTemp = []
dataWindspeed = []
windDir = []
conditions = []

lines =  data.readlines()
countlines = 0
for line in lines[162:177]:                  #reads data into lists
    strings = line.split(",")
    dataTemp.append(strings[2])
    dataWindspeed.append(strings[12])
    windDir.append(strings[13])
    conditions.append(strings[22])
    countlines += 1

print(countlines)
    


#measure the general conditions

amount_clear = conditions.count("clear-day") + conditions.count("clear-night")
amount_cloudy = conditions.count("cloudy")
amount_partially_cloudy = conditions.count("partly-cloudy-day") + conditions.count("partly-cloudy-night")
amount_rain = conditions.count("rain")



if amount_clear == countlines:
    print("Es wird den ganzen Tag die Sonne scheinen")
elif amount_cloudy == countlines:
    print("It will be Overcast all day")
elif amount_partially_cloudy == countlines:
    print("Es wird den ganzen Tag Teils Bewölkt sein")
elif (countlines/amount_cloudy + amount_partially_cloudy) > 0.7:
    print("Es wird teilweise Bewölkt sein")
else:
    print("Das Wetter ist anders")

amount_rest = countlines - (amount_clear + amount_cloudy + amount_partially_cloudy)

print("Stunden klar:",amount_clear,"\n""Stunden bewölkt:",amount_cloudy,"\nStunden teilweise bewölkt:",amount_partially_cloudy,"\nRegenstunden:",amount_rain,"\nRest:",amount_rest) #,sep="\t")




#print(dataTemp)
#print()
#print(dataWindspeed)
#print()
#print(windDir)
#print()
#print(conditions)
#print(text)


