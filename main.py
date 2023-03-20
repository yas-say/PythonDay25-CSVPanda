# # with open('weather_data.csv') as file:
# #     data = file.readlines()
# #
# # print(data)
#
# # import csv
# #
# # temperature = []
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #
# # # temperature.pop(0)
# # #
# # # for i in range(0,len(temperature)):
# # #     temperature[i] = int(temperature[i])
# #
# # print(temperature)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# # ctr = 0
# # sum = 0
# # for _ in data_list:
# #     sum += _
# #     ctr += 1
# #
# # # print(f"Avergae is {sum/ctr}")
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # # Get Row
# # print(data[data.day == "Monday"])
# #
# # print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
# print(f"Temp in f: {(int(monday.temp) * 1.8) + 32}")


import pandas

color = ["Gray", "Black", "Cinnamon"]
dict= dict(Color=[], Count=[])
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data_series)
# print(data_series.count())
# print(data_series[data_series["Primary Fur Color"]=="Cinnamon"].count())
for _ in color:
    data_series = data[data["Primary Fur Color"]==_]["Primary Fur Color"]
    dict["Color"].append(_)
    dict["Count"].append(data_series.count())

print(dict)

data_dict = pandas.DataFrame(dict)
data_dict.to_csv("new_data.csv")

