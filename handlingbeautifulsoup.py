# HOW TO WEBSCARPPING USING BEAUTIFULsoup FROM HTML WEB
# pip3 install beautifulsoup4
# pip3 install requests

from bs4 import BeautifulSoup # webscrapping
import requests # crawler

def printH1Tags(soup):
    h1tags = soup.find_all('h1')
    for h1tag in h1tags:
        print(h1tag.text)

def printH2Tags(soup):
    h2tags = soup.find_all('h2')
    for h2tag in h2tags:
        print(h2tag.text)

def printAllLinks(soup):
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

url = "https://www.w3schools.com/python/default.asp"
response = requests.get(url) # crawl and download the html source
html_content = response.text

# let us scrapp the html source and find the information inside the
# html source
soup = BeautifulSoup(html_content, 'html.parser')
printH1Tags(soup)
printH2Tags(soup)
printAllLinks(soup)
