# proto script to querry a webpage for the current position of the ISS.
# Eventually this coordinate will be passed to an arduino which will light
# up a corresponding LED on a world map to the ISS location.
# Might need to add a library capable of scraping javascript webpages.

import requests
from bs4 import BeautifulSoup

r = requests.get("http://iss.astroviewer.net/")

r.content #prints all content r

soup = BeautifulSoup(r.content, 'html.parser')

soup.find_all("a") #finds all instances of "a", in html this will be links

for link in soup.find_all("a"):  #loops though "a" and prints each link
  print(link)

for link in soup.find_all("a"): #loops through "a" and prints hrefs
  link.get("href")

for link in soup.find_all("a"): #shows text of each link
  print(link.text)

for link in soup.find_all("a"):
    print(link.text, link.get("href"))

print(link.content[0].text)

location = soup.find_all("div", {"id":"cockpit"}) #isolates the cockpit div
for item in location:
    print(item.contents[3]) #that's the line with the location data
