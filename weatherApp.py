import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/en-IN/weather/today/l/5b820928fa0d62db5f789c705901d462a1132494082633c46cc2c5e8b8c14546"
master = Tk()
master.title("Weather App")
master.config(bg = "white")
'''
img = Image.open("D:\Python Codes\weatherApp.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)
'''

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--2_osB").text
    temperature = soup.find('span', class_ = "CurrentConditions--tempValue--1RYJJ").text
    weatherPrediction = soup.find('div', class_ = "CurrentConditions--phraseValue--17s79").text
    

    #Now we have to put all this gathered information onto our labels

    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPrediction)

    temperatureLabel.after(60000, getWeather) #60000 ms = 60 sec, after means after the mentioned duration
    master.update()
    return weatherPrediction
    

#LocationLabel
locationLabel = Label(master,font = ("Calibri bold", 20), bg = "white")
locationLabel.grid(row = 0, sticky = "N", padx = 100)

#temperatureLabel
temperatureLabel = Label(master,font = ("Calibri bold", 70), bg = "white")
temperatureLabel.grid(row = 1, sticky = "W", padx = 40)

#weatherPredictionLabel
weatherPredictionLabel = Label(master, font = ("Calibri bold", 20), bg = "white")
weatherPredictionLabel.grid(row = 2, sticky = "W", padx = 40)
c = getWeather()


if("Drizzle" in c):
    img = Image.open("D:\Python Codes\icons\Drizzle.png")
elif("Sun" in c):
    img = Image.open("D:\Python Codes\icons\Sunny.png")
elif("Rain" in c):
    img = Image.open("D:\Python Codes\icons\Rainy.png")
elif("Partly" in c):
    img = Image.open("D:\Python Codes\icons\PartlyCloudy.png")
elif("Cloud" in c):
    img = Image.open("D:\Python Codes\icons\Cloudy.png")
elif("Wind" in c):
    img = Image.open("D:\Python Codes\icons\Windy.png")
elif("Haze" in c):
    img = Image.open("D:\Python Codes\icons\Haze.jpg")
else:
    img = Image.open("D:\Python Codes\weatherApp.png")


    
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)
Label(master, image = img, bg = "white").grid(row = 1, sticky = "E")

master.mainloop()
