# in keyword and iterations in dictionary 

user_info = {
    'name' : 'Pranjal',
    'age' : 18, 
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# check if key exist in dictionary
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# check if value exist  in dictionary   ---> values method 
# if 24 in user_info.values():
#     print('present')
# else:
#     print('not present')

# values method  
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# loops in dictionaries
# for i in user_info:
#     print(user_info[i])

# items method 
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))
# [('name', 'Pranjal'), ('age', 18), ('fav_movies', ['coco', 'kimi no na wa']), ('fav_tunes', ['awakening', 'fairy tale'])]

for i, j in user_info.items():
    print(f"key is {i} and value is {j} ")