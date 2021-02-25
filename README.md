# Volcanoes and World Population Web Map on Broswer

Used Libraries: 
* Folium - It's used to create the web map.
* Pandas - It's used to read data. 
* Requests, BeautifulSoup - They're used for web scraping.  
 
In this project, a web map which shows volcanoes and world population in seperated layers is created by using Folium on Python. World.json file is used for population of countries.  

![map1](https://user-images.githubusercontent.com/78566362/109129895-2f5c2380-7762-11eb-8ce5-c1021946683d.jpg)

Volcanoes and countries are clasified based on evelation and population respectively in colors.

![map2](https://user-images.githubusercontent.com/78566362/109129899-308d5080-7762-11eb-9ee2-d6cea20bfd7b.jpg)

Volcanoes' name, evelation, location, latitude and longitude informations are stored in data.txt by using web scraping. And the data is used to create markers on map. Volcanoes' names on popup are linked to a Google search for more informations. 

![map3](https://user-images.githubusercontent.com/78566362/109129903-3125e700-7762-11eb-80f1-4ee8914a34af.jpg)
