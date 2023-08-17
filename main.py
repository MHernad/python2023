import requests
import pandas as pd

season = 2002

mydataset = {
    'season': [],
    'champion': []
}

while season < 2023:
    url = "https://api-football-standings.azharimm.dev/leagues/eng.1/standings?season={_season}&sort=asc".format(_season=season)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        txt = str(data["data"])
        txt = txt.split(",")
        txt = txt[7]
        txt = txt.split("'")
        mydataset["season"].append(season)
        mydataset["champion"].append(txt[3])

    season += 1

df = pd.DataFrame(mydataset)

df.to_csv('campeonesIngleses.csv')
