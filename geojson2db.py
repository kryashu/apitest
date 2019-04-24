import json
import psycopg2
#Connection to database test
try: 
 conn= psycopg2.connect(database="test", user="postgres", password="1234", host="127.0.0.1", port="5432")
except Exception as e:
    print e
cur=conn.cursor()
sql = "Insert into geo values(%s,%s,%s,%s);"

with open('geojson.json') as f:
    data = json.load(f)

for feature in data['features']:
    name= feature['properties']['name']
    parent= feature['properties']['parent']
    ty =  feature['geometry']['type']
    co_list = feature['geometry']['coordinates']
    for i in co_list:
        coordinates=i
    cur.execute(sql,[str(name),str(parent),str(ty),coordinates])
    conn.commit()
conn.close()
