#Go to https://petitions.whitehouse.gov/petitions
#Go to the petition page for each of the petitions.
#Create a .csvle with the following information for each petition:
    #Title
    #Published date
    #Issues
    #Number of signatures

from bs4 import BeautifulSoup
import urllib.request
import csv
import unicodedata

with open('hw2_jordan.csv', 'w', encoding='utf-8') as f:
  w = csv.DictWriter(f, fieldnames = ("title", "date", "firstissue", "secondissue", "thirdissue", "signatures"))
  w.writeheader()
  web_address1 = 'https://petitions.whitehouse.gov/petitions?page=1'
  petitions1 = {}
  web_page1 = urllib.request.urlopen(web_address1)
  all_html1 = BeautifulSoup(web_page1.read())
  all_petitions1 = all_html1.find_all('h3')
  for j in all_petitions1:
      all_az1 = j.find_all('a')
      for az1 in all_az1:
          petitions_address1 = "https://petitions.whitehouse.gov/" + az1['href']
          petitions_page1 = urllib.request.urlopen(petitions_address1)
          petitions_html1 = BeautifulSoup(petitions_page1.read())
          petitions1['title'] = petitions_html1.find('h1').get_text()
          petitions1['date'] = petitions_html1.find('h4').get_text()[19:]
          issues1 = petitions_html1.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
          all_h61 = issues1.find_all('h6')
          petitions1['firstissue'] = unicodedata.normalize('NFKD', all_h61[0].get_text())
          try:
              petitions1['secondissue'] = unicodedata.normalize('NFKD', all_h61[1].get_text())
          except IndexError:
              petitions1['secondissue'] = 'NA'
          try:
              petitions1['thirdissue'] = unicodedata.normalize('NFKD', all_h61[2].get_text())
          except IndexError:
              petitions1['thirdissue'] = 'NA'
          petitions1['signatures'] = petitions_html1.find('span', {'class' : 'signatures-number'}).get_text()
          w.writerow(petitions1)
  web_address2 = 'https://petitions.whitehouse.gov/petitions?page=2'
  petitions2 = {}
  web_page2 = urllib.request.urlopen(web_address2)
  all_html2 = BeautifulSoup(web_page2.read())
  all_petitions2 = all_html2.find_all('h3')
  for j in all_petitions2:
      all_az2 = j.find_all('a')
      for az2 in all_az2:
          petitions_address2 = "https://petitions.whitehouse.gov/" + az2['href']
          petitions_page2 = urllib.request.urlopen(petitions_address2)
          petitions_html2 = BeautifulSoup(petitions_page2.read())
          petitions2['title'] = petitions_html2.find('h1').get_text()
          petitions2['date'] = petitions_html2.find('h4').get_text()[19:]
          issues2 = petitions_html2.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
          all_h62 = issues2.find_all('h6')
          petitions2['firstissue'] = unicodedata.normalize('NFKD', all_h62[0].get_text())
          try:
              petitions2['secondissue'] = unicodedata.normalize('NFKD', all_h62[1].get_text())
          except IndexError:
              petitions2['secondissue'] = 'NA'
          try:
              petitions2['thirdissue'] = unicodedata.normalize('NFKD', all_h62[2].get_text())
          except IndexError:
              petitions2['thirdissue'] = 'NA'
          petitions2['signatures'] = petitions_html2.find('span', {'class' : 'signatures-number'}).get_text()
          w.writerow(petitions2)
  web_address3 = 'https://petitions.whitehouse.gov/petitions?page=3'
  petitions3 = {}
  web_page3 = urllib.request.urlopen(web_address3)
  all_html3 = BeautifulSoup(web_page3.read())
  all_petitions3 = all_html3.find_all('h3')
  for j in all_petitions3:
      all_az3 = j.find_all('a')
      for az3 in all_az3:
          petitions_address3 = "https://petitions.whitehouse.gov/" + az3['href']
          petitions_page3 = urllib.request.urlopen(petitions_address3)
          petitions_html3 = BeautifulSoup(petitions_page3.read())
          petitions3['title'] = petitions_html3.find('h1').get_text()
          petitions3['date'] = petitions_html3.find('h4').get_text()[19:]
          issues3 = petitions_html3.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
          all_h63 = issues3.find_all('h6')
          petitions3['firstissue'] = unicodedata.normalize('NFKD', all_h63[0].get_text())
          try:
              petitions3['secondissue'] = unicodedata.normalize('NFKD', all_h63[1].get_text())
          except IndexError:
              petitions3['secondissue'] = 'NA'
          try:
              petitions3['thirdissue'] = unicodedata.normalize('NFKD', all_h63[2].get_text())
          except IndexError:
              petitions3['thirdissue'] = 'NA'
          petitions3['signatures'] = petitions_html3.find('span', {'class' : 'signatures-number'}).get_text()
          w.writerow(petitions3)
  web_address4 = 'https://petitions.whitehouse.gov/petitions?page=4'
  petitions4 = {}
  web_page4 = urllib.request.urlopen(web_address4)
  all_html4 = BeautifulSoup(web_page4.read())
  all_petitions4 = all_html4.find_all('h3')
  for j in all_petitions4:
      all_az4 = j.find_all('a')
      for az4 in all_az4:
          petitions_address4 = "https://petitions.whitehouse.gov/" + az4['href']
          petitions_page4 = urllib.request.urlopen(petitions_address4)
          petitions_html4 = BeautifulSoup(petitions_page4.read())
          petitions4['title'] = petitions_html4.find('h1').get_text()
          petitions4['date'] = petitions_html4.find('h4').get_text()[19:]
          issues4 = petitions_html4.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
          all_h64 = issues4.find_all('h6')
          petitions4['firstissue'] = unicodedata.normalize('NFKD', all_h64[0].get_text())
          try:
              petitions4['secondissue'] = unicodedata.normalize('NFKD', all_h64[1].get_text())
          except IndexError:
              petitions4['secondissue'] = 'NA'
          try:
              petitions4['thirdissue'] = unicodedata.normalize('NFKD', all_h64[2].get_text())
          except IndexError:
              petitions4['thirdissue'] = 'NA'
          petitions4['signatures'] = petitions_html4.find('span', {'class' : 'signatures-number'}).get_text()
          w.writerow(petitions4)
  web_address5 = 'https://petitions.whitehouse.gov/petitions?page=5'
  petitions5 = {}
  web_page5 = urllib.request.urlopen(web_address5)
  all_html5 = BeautifulSoup(web_page5.read())
  all_petitions5 = all_html5.find_all('h3')
  for j in all_petitions5:
      all_az5 = j.find_all('a')
      for az5 in all_az5:
          petitions_address5 = "https://petitions.whitehouse.gov/" + az5['href']
          petitions_page5 = urllib.request.urlopen(petitions_address5)
          petitions_html5 = BeautifulSoup(petitions_page5.read())
          petitions5['title'] = petitions_html5.find('h1').get_text()
          petitions5['date'] = petitions_html5.find('h4').get_text()[19:]
          issues5 = petitions_html5.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
          all_h65 = issues5.find_all('h6')
          petitions5['firstissue'] = unicodedata.normalize('NFKD', all_h65[0].get_text())
          try:
              petitions5['secondissue'] = unicodedata.normalize('NFKD', all_h65[1].get_text())
          except IndexError:
              petitions5['secondissue'] = 'NA'
          try:
              petitions5['thirdissue'] = unicodedata.normalize('NFKD', all_h65[2].get_text())
          except IndexError:
              petitions5['thirdissue'] = 'NA'
          petitions5['signatures'] = petitions_html5.find('span', {'class' : 'signatures-number'}).get_text()
          w.writerow(petitions5)
