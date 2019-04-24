from flask import Flask,request
import json
import psycopg2
#Connection to database test
try: 
 conn= psycopg2.connect(database="test", user="postgres", password="1234", host="127.0.0.1", port="5432")
except Exception as e:
    print e
cur=conn.cursor()

app= Flask(__name__)


@app.route('/post_location', methods=['POST'])
def post_location():
    pin = request.json['key']
    add = request.json['add']
    city = request.json['city']
    lat = request.json['lat']
    lng = request.json['lng']
    
    sql1="Select * from main where key = %s;"
    sql2 = "Inster into main (%s,%s,%s,%s,%s);"
    cur.execute(sql1,[pin])
    if cur.fetchall():
        return "Pin Code already Exists"
    else:
        cur.execute(sql2,[pin,add,city,lat,lng])
        conn.commit()
        return "Request Approved"
    
@app.route('/get_using_postgres/<lat>/<lng>',methods=['get'])
def get_using_postgres(lat,lng):
    cur.execute('create extension cube;')
    cur.execute('create extension earthdistance;')
    sql = "Select key from main where (point(%s,%s) <@> point(cast(longitude as DOUBLE PRECISION),cast(latitude as DOUBLE PRECISION)))<= 5;"
    cur.execute(sql,[lng,lat])
    data = json.dumps(cur.fetchall())
    return data
if __name__ == '__main__':
    app.run(host='localhost',port='8080',debug=True)
