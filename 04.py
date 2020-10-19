import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"
print("Hello! Please choose select a country by number!")
result = requests.get(url)
result_soup = BeautifulSoup(result.text, "html.parser")

table = result_soup.find_all("tr")

country = []

for item in table[1:]:
  try:
    country.append(item.find_all('td')[:-1])
  except:
    pass


delete_lst = []
for n, item in enumerate(country):
  for m, i in enumerate(item):
    country[n][m] = i.string
    if country[n][2] == None:
      delete_lst.append(n)

for i in delete_lst:
  del country[i]

# print(country)
for i, item in enumerate(country):
  print("#", i, item[0][0] + item[0][1:].lower())


def query():
  try:
    a = int(input("#: "))
    if a not in range(1, i+1):
      print("Choose a number from the list.")
      query()
    else:
      print("You chose " + country[a][0].lower())
      print("The currency code is " + country[a][2])
  except:
    print("That wasn't a number.")
    query()

query()
