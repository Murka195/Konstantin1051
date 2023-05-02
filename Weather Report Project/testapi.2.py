
import requests

response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/19122/tomorrow?unitGroup=metric&include=hours&key=7Z8KKMD3WEEF2ZYRNC25DVVRF&contentType=csv")
data = response.json()

print(data)

for i in data:
    #print(i)
    #print("hallo")
    pass



#response = respo





'''pip install requests


#pip install requests
#conda install requests
import requests

link = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/19122?unitGroup=metric&include=hours&key=7Z8KKMD3WEEF2ZYRNC25DVVRF&contentType=csv"

response = requests.get(link)

print(response.status_code)

'''