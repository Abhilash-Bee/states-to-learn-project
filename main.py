# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for day, temp, weather in data:
#         if temp.isnumeric():
#             temperature.append(int(temp))
#
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
# print(data_list)

# print(f"Average temperature = {round(sum(data_list)/len(data_list), 2)}")

# print(f"Average temperature = {data['temp'].mean()}")
#
# print(f"Max temperature = {data['temp'].max()}")
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Print the row which has the highest temperature
# print(data[data.temp == data.temp.max()])

# data_list = {
#     "Name": ["Angela", "Tim", "Navin"],
#     "Score": [90, 80, 10],
# }
#
# data = pandas.DataFrame(data_list)
# print(data)

data = pandas.read_csv("squirrel_data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color_count, cinnamon_color_count, black_color_count],
}

pandas.DataFrame(data_dict).to_csv("final_gen.csv")

# data_dict = {}
#
# for color in color_list:
#     if color in ["Gray", "Cinnamon", "Black"]:
#         data_dict[color] = data_dict.setdefault(color, 0) + 1
#
# final_dict = {
#     "Fur color": [],
#     "Count": [],
# }
#
# for key, value in data_dict.items():
#     final_dict["Fur color"].append(key)
#     final_dict["Count"].append(value)
#
# pandas.DataFrame(final_dict).to_csv("final_gen.csv")
