import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.statscrew.com/football/roster/t-PIT/y-2020'#your url
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


#player_table = soup.select('tbody')
#links = player_table.find_all('a')
#links = [l.get('href') for l in links]



stats = soup.find('tbody')

masterlist = []


i = 0

while i < 54:

    player = stats.select('tr')[i]

    for v in player:
        sublist = {}

        sublist['Number'] = player.find_all("td", {'class':'dt-right'})[0].text
        sublist['Rank'] = player.find_all("td", {'class': 'dt-right'})[1].text
        sublist['Name'] = player.find_all("td", {'class': 'dt-left'})[0].text
        sublist['Position'] = player.find_all("td", {'class': 'dt-left'})[1].text
        sublist['DOB'] = player.find_all("td", {'class': 'dt-left'})[2].text
        sublist['Height'] = player.find_all("td", {'class': 'dt-left'})[4].text
        sublist['Location'] = player.find_all("td", {'class': 'dt-left'})[4].text

    masterlist.append(sublist)
    i = i + 1


print(masterlist)

df = pd.DataFrame(masterlist)

df.to_csv('sample2.csv', index=False)
