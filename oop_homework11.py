import json
import os
import sqlite3
from sqlite3 import Error
import sys
import pprint

database = os.path.join(os.getcwd(), "database_new/film_data.db")
print(database)

try:
    connection = sqlite3.connect(database)
except Error as err:
    print(err)
    sys.exit()

curs = connection.cursor()

# Ex. 1
# starts_with_b = """SELECT title
#                     FROM film_data
#                     WHERE title like "B%"
# """
# result = curs.execute(starts_with_b)
# pprint.pprint(result.fetchall())

# Ex. 2
# largest_duration = """SELECT length
#                     FROM film_data
#                     ORDER BY length desc
# """
#
# result_ = curs.execute(largest_duration)
# pprint.pprint(result_.fetchone())

# Ex. 3
# films = """SELECT *
#             FROM film_data
#         """
# res = curs.execute(films)
# data = res.fetchall()
# # pprint.pprint(data)
# data_2 = str(data)
#
# with open("films.txt", "w") as films:
#     films.write(data_2)
#
#
# with open("films.json", "w") as film:
#     json.dump(films, film)


# # # Extra Homework

# update_rate = """UPDATE film_data
#                     SET release_year = 2018
#                     WHERE film_id = 133
#                 """
# curs.execute(update_rate)
# connection.commit()

# write_in_new_table = """SELECT *
#                         FROM film_data
#                         WHERE release_year >= 2010 and rate between "3" and "5"
# """
#
#
# result_ = curs.execute(write_in_new_table)
# pprint.pprint(result_.fetchall())

# new_table = """CREATE TABLE IF NOT EXISTS filtered_films (
#                                 films_id integer,
#                                 title text,
#                                 description text,
#                                 release_year integer,
#                                 length integer,
#                                 rate integer,
#                                 special_features text
#
#                 ); """

# curs.execute(new_table)
# connection.commit()

# insert_old_ = """INSERT INTO filtered_films
#                 SELECT film_id, title, description, release_year, length, rate, special_features
#                 FROM film_data
#                 WHERE release_year >= 2010 and rate between "3" and "5"
#                 """
#
# curs.execute(insert_old_)
# connection.commit()





