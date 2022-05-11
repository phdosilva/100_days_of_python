# How to raise your own exception

# height = float(input())
# weight = float(input())
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 metters")
#
# bmi = weight / height ** 2
# print(bmi)

# Exception Handling

# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + "pie")
#
#
# make_pie(2)

# Key Error Handling

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes += 0
#
# print(total_likes)
