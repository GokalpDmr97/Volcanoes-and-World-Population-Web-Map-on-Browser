import requests
from bs4 import BeautifulSoup

#You can find all volcano informations by visiting the website. 
url = "http://volcano.oregonstate.edu/volcano_table" 

#Web Scraping
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("table",{"class":"views-table cols-6"}).find("tbody").find_all("tr")


names,elevations,latitudes,longitudes,locations = [],[],[],[],[]
list_names = [elevations,latitudes,longitudes,locations,names]

for tr in list:
    names.append(tr.find("td",{"class":"views-field views-field-title"}).find("a").text)
    elevations.append(tr.find("td",{"views-field views-field-field-elevation-value"}).text.strip())
    latitudes.append(tr.find("td",{"views-field views-field-field-latitude-value"}).text.strip())
    longitudes.append(tr.find("td",{"views-field views-field-field-longitude-value"}).text.strip())
    locations.append(tr.find("td",{"views-field views-field-field-location-value"}).text.strip())


#Cleaning data from empty values.

empty_indexes = []
for lst in list_names:
    for index in [i for i,x in enumerate(lst) if x==""]: 
        if index not in empty_indexes:
            empty_indexes.append(index)
                
[[lst.pop(i) for i in sorted(empty_indexes, reverse=True)] for lst in list_names]

#Creating the file 
with open("volcanoes.txt","a+",encoding ="utf-8") as volcanos_file:
    volcanos_file.write("NAME,LOCATION,ELEV,LAT,LON\n")
    for nm,loc,el,lat,lon in zip(names,locations,elevations,latitudes,longitudes):
        volcanos_file.write(f"{nm},{loc},{el},{lat},{lon}\n")

