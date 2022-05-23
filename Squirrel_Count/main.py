# Counts the number of gray, cinnamon, and black squirrels from 2018 Central Park Squirrel Census using pandas
# Outputs to newfile.csv

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_series = data["Primary Fur Color"].dropna()
unique_colors = fur_series.unique()
print(unique_colors)

gray = fur_series[fur_series == "Gray"].count()
cinnamon = fur_series[fur_series == "Cinnamon"].count()
black = fur_series[fur_series == "Black"].count()
colors = [gray, cinnamon, black]
# color_table = {"colors":unique_colors, "count":colors}
color_table = [unique_colors, colors]
print(color_table)

pd_color_table = pandas.DataFrame(color_table)
pd_color_table.to_csv("furcolors.csv")

