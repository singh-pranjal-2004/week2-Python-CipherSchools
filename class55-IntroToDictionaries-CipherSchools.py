# dictionaries intro
# Q - why we use dictionaries?
# A - Because of limitations of lists , lists are not enough to represent 
# real data .

# Example
user = ['Pranjal', 18, ['coco', 'kimi no na wala'], ['awakening', 'fairy tale']]
# this list contains user name, age , fav movies , fav tunes 
# you can do this but this is not a good way to do this.


# Q - what are dictionaries
# A - unordered collections of data in key : value pair.


# how to create dictionaries 
user = {'name' : 'Pranjal', 'age' : 18}
# print(user)
# print(type(user))


# second method to create dictionary
user1 = dict(name = 'Pranjal', age = 18)
# print(user1)


# how to access data from dictionary 
# NOTE - There is no indexing because of unordered collections of data.
# print(user['name'])
# print(user['age'])

# which type of data a dictionary can store ?
# anything
# numbers, strings, list, dictionary

user_info = {
    'name' : 'Pranjal',
    'age' : 18, 
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}
# print(user_info['fav_movies'])



# How to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'Pranjal'
user_info2['age'] = 18

print(user_info2)