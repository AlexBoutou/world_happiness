import json
import pandas

with open('./data/world_countries.json', 'r') as f:
    world_countries = json.load(f)

    years = [2015, 2016, 2017, 2018, 2019]

    for year in years:
        df = pandas.read_csv('./data/{}.csv'.format(year), header=0)
        for country in world_countries["features"]:
            try:
                country["properties"]["HS {}".format(year)] = float(df.loc[df["Country"] == country["properties"]["name"]]["Happiness Score"])
            except TypeError:
                pass

    with open("./data/new_world_countries.json", "wb") as file:
        file.write(json.dumps(world_countries).encode("utf-8"))
