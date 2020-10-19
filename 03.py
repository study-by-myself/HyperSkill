import requests
import os

def is_it_down():
  a = input("Welcome to IsItDown.py! \nPlease write a URLs you want to check (separated by comma)\n")

  input_list = a.split(',')
  for i, url in enumerate(input_list):
    input_list[i] = url.strip()
  list_len = len(input_list)
  if list_len > 1:
    for i in range(list_len):
      try:
        r = requests.get("http://" + input_list[i])
        if r.status_code == 200:
          print("http://" + input_list[i] + " is up!")
      except:
        print(input_list[i] + " is down!")

  else:
    try:
      r = requests.get("http://" + input_list[0])
      if r.status_code == 200:
        print("http://" + input_list[i] + " is up!")
        
    except:
      print(input_list[i] + " is not a valid URL.")
  end_query()

def end_query():
  answer = input("Do you want to start over? y/n ")
  if answer == 'y':
    os.system('clear')
    is_it_down()
  elif answer == 'n':
    print("k, bye!")
  else:
    print("That's not a valid answer!")
    end_query()

is_it_down()
