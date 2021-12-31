import pandas


data = pandas.read_csv("weather_data.csv")
print(data.to_dict())

temp_list = data["temp"]
print(temp_list.mean())
print(temp_list.max())

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("students_score.csv")
