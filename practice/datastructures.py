day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]  # list

day_of_week.append("Sat")
print(day_of_week)
day_of_week.append("Sun")
print(day_of_week)
day_of_week.remove("Sun")
print(day_of_week)

days = ("Mon", "Tue", "Wed")  # Tuple 튜플은 불변하다

# dictionary key:value
player = {
    'name': 'nioc',
    'age': 12,
    'alive': True,
    "fav_food": ["piZ", "hamburger"],
    "friend": {
        "name": "lynn",
        "fav_food": ["apple"]
    }
}
print(player.get('age'))
print(player.get('fav_food'))
print(player['fav_food'])
print(player)
print(player["friend"])
print(player["friend"]["fav_food"])

player["fav_food"].append("noodle")  # list에 값 추가
print(player["fav_food"])
player['xp'] = 1500  # key 추가
