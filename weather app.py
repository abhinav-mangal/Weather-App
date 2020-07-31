import requests
from bs4 import BeautifulSoup


def Weather_App() :
    u = "weather of " + input('Enter name of your CITY: ')
    print('Processing..')

    url = f"https://www.google.com/search?q={u}"

    r = requests.get(url)

    s = BeautifulSoup(r.text, "html.parser")

    f = s.find('div', class_="BNeawe").text
    print(f)


Weather_App()
