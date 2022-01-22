from dotenv import dotenv_values  # pip install python-dotenv
import mysql.connector  # pip install mysql-connector-python
from sqlqueries import *

config = dotenv_values('.env')
cnx = mysql.connector.connect(user=config['USER'], password=config['PASSWORD'],
                              host=config['HOST'],
                              database=config['DATABASE'],
                              ssl_disabled=True)

cursor = cnx.cursor()

cursor.execute(query_foreign_key_check_0)
cursor.execute(query_turncate_category)
cursor.execute(query_turncate_course)
cursor.execute(query_turncate_ingredient)
cursor.execute(query_turncate_measurement_unit)
cursor.execute(query_turncate_recipe)
cursor.execute(query_turncate_ingredient_recipe)
cursor.execute(query_foreign_key_check_1)
cursor.execute(query_populate_category)
cursor.execute(query_populate_course)
cursor.execute(query_populate_ingredient)
cursor.execute(query_populate_unit)
cursor.execute(query_populate_recipe)
cursor.execute(query_populate_ingredient_recipe)

cnx.commit()
cursor.close()
cnx.close()
