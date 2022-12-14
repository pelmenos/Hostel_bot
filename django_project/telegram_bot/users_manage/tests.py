import psycopg2
import sqlite3

# conn = psycopg2.connect("dbname=Hostel user=postgres password=animeshnik666")
# conn_lite = sqlite3.connect('db.sqlite3')
# cur = conn.cursor()
# cursor = conn_lite.cursor()
# asd = cursor.execute('SELECT * from sql_recipe_tag').fetchall()
# for i in asd:
#     cur.execute("INSERT INTO users_manage_recipe_tag (recipe_id, tag_id) VALUES (%s, %s)", (i[1], i[2]))
#     conn.commit()
# conn_lite.close()
# cur.close()
# conn.close()


conn_lite = sqlite3.connect('db.sqlite3')
cursor = conn_lite.cursor()
asd = cursor.execute('SELECT recipe from sql_recipe').fetchall()
for i in asd:
    print((len(i[0]) + len('Рецепт:\n')))
conn_lite.close()
