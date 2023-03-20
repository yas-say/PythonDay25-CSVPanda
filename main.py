# with open('weather_data.csv') as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# temperature = []
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# # temperature.pop(0)
# #
# # for i in range(0,len(temperature)):
# #     temperature[i] = int(temperature[i])
#
# print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

