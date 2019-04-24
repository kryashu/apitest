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

def isInside(self, border, target):
 degree = 0
 for i in range(len(border) - 1):
    a = border[i]
    b = border[i + 1]

    # calculate distance of vector
    A = getDistance(a[0], a[1], b[0], b[1]);
    B = getDistance(target[0], target[1], a[0], a[1])
    C = getDistance(target[0], target[1], b[0], b[1])

    # calculate direction of vector
    ta_x = a[0] - target[0]
    ta_y = a[1] - target[1]
    tb_x = b[0] - target[0]
    tb_y = b[1] - target[1]

    cross = tb_y * ta_x - tb_x * ta_y
    clockwise = cross < 0

    # calculate sum of angles
    if(clockwise):
        degree = degree + math.degrees(math.acos((B * B + C * C - A * A) / (2.0 * B * C)))
    else:
        degree = degree - math.degrees(math.acos((B * B + C * C - A * A) / (2.0 * B * C)))

 if(abs(round(degree) - 360) <= 3):
    return True
 return False

@app.route('/check/<lat>/<lng>',methods=['get'])
def check(lat,lng):
   sql = "Select * from geo;"
   cur.execute(sql)
   for i in cur.fetchall():
    fli=[]
    for n in range(0,len(i[3])):
     for x in range(0,len(i[3][n])):
      li=[]
      for y in i[3][n]:
          
          li.append(float(y))
     fli.append(li)
    if isInside(fli,[lng,lat]):
        d={"city":i[0],"parent":i[1]}
        return json.loads(d)
    else:
        pass

if __name__ == '__main__':
    app.run(host='localhost',port='8080',debug=True)
