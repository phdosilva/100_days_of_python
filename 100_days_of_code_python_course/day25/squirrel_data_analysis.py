import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_column = data["Primary Fur Color"]

new_data = dict({
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [len(color_column[color_column == "Black"]),
              len(color_column[color_column == "Gray"]),
              len(color_column[color_column == "Cinnamon"])]
})

pandas.DataFrame(new_data).to_csv("squirrel_count.csv")
