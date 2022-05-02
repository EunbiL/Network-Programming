'''
Exercice 2 - Analyze XML
'''

#1. retrieve the content of the page
import xml.etree.ElementTree as ET
doc = ET.parse("cd.xml")
root = doc.getroot()

#2. display for each CD: title, artist, country, company, year
for cd in root.iter("CD") :
    print("="*50)
    print("Title :", cd.findtext("TITLE"))
    print("Artist : ", cd.findtext("ARTIST"))
    print("Country : ", cd.findtext("COUNTRY"))
    print("Company : ", cd.findtext("COMPANY"))
    print("Year : ", cd.findtext("YEAR"))
print('='*50)

#3. Display all 1980 CDs
print("These CDs are 1980s")
for cd in root.iter("CD") :
    year = int(cd.findtext("YEAR"))
    if (year >= 1980 and year < 1990) :
        print("Title:", cd.findtext("TITLE"),",Year:", cd.findtext("YEAR"))
print("="*50)

#4. display all british CDs
print("voila, These CDs are british")
for cd in root.iter("CD") :
    if cd.findtext("COUNTRY") == "UK" :
        print("Title:", cd.findtext("TITLE"), ",Country:", cd.findtext("COUNTRY"))


