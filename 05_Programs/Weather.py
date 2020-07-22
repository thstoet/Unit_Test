import requests
from bs4 import BeautifulSoup

def dispTranslator(data):
    new_dict = dict()
    new_dict.update([("bedeckt", "x")])

    return new_dict[data]


if __name__ == "__main__":

    URL_weather = "https://www.wetter.com/deutschland/leipzig/DE0006194.html"

    page = requests.get(URL_weather)
    soup = BeautifulSoup(page.content, 'html.parser')

    # elems = soup.find_all('table', class_='weather-overview mb mt')
    elems = soup.find_all('td', class_="text--center pb-- tdbl")

    x = 0
    for elem in elems:
        if x == 2:
            break
        icon = elem.find('img', alt=True)
        data = icon['alt']
        icon_disp = dispTranslator(data)
        print(icon_disp)
        x += 1


