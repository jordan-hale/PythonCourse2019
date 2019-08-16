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
#opens csv with the following columns
with open('hw2_jordan.csv', 'w', encoding='utf-8') as f:
  w = csv.DictWriter(f, fieldnames = ("title", "date", "firstissue", "secondissue", "thirdissue", "signatures"))
  w.writeheader()
#starts for loop to iterate over each of the four pages
  pages = ['page=0','page=1','page=2','page=3','page=4']
  for i in range(0,5):
      extension = pages[i]
      web_address = 'https://petitions.whitehouse.gov/petitions?%s' %extension
#starts a dictionary for the petitions from each page
      petitions = {}
#navigates to each petition's url
      web_page = urllib.request.urlopen(web_address)
      all_html = BeautifulSoup(web_page.read())
      all_petitions = all_html.find_all('h3')
      for j in all_petitions:
          all_az = j.find_all('a')
          for az in all_az:
              petitions_address = "https://petitions.whitehouse.gov/" + az['href']
              petitions_page = urllib.request.urlopen(petitions_address)
              petitions_html = BeautifulSoup(petitions_page.read())
#pulls the title
              petitions['title'] = petitions_html.find('h1').get_text()
#pulls the date
              petitions['date'] = petitions_html.find('h4').get_text()[19:]
#pulls the issues (up to 3)
              issues = petitions_html.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
              all_h6 = issues.find_all('h6')
              petitions['firstissue'] = unicodedata.normalize('NFKD', all_h6[0].get_text())
              try:
                  petitions['secondissue'] = unicodedata.normalize('NFKD', all_h6[1].get_text())
              except IndexError:
                  petitions['secondissue'] = 'NA'
              try:
                  petitions['thirdissue'] = unicodedata.normalize('NFKD', all_h6[2].get_text())
              except IndexError:
                  petitions['thirdissue'] = 'NA'
#pulls the signatures
              petitions['signatures'] = petitions_html.find('span', {'class' : 'signatures-number'}).get_text()
#fills in the csv
              w.writerow(petitions)
