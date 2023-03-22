from flask import Flask, render_template, request 
import pymssql

app = Flask(__name__)
app.secret_key = "asdgfjhsdgfjhsdgryaesjtrjyetrjyestrajyrtesyjrtdyjrtasdyrtjsejrtestrerty"
header_html = '<html> <head> <title> Assignment4</title> </head> <body> <h1> ID: 1002034491 </h1> <h1> Name:Avinash Reddy Sallagonda </h1> <br />'
server='assmt-3.database.windows.net'
db='assignment-3'
user='rootsql'
password='Salla@2022@'
conn = pymssql.connect(server,user,password,"assignment-3")
c1 = conn.cursor()

@app.route('/', methods=['GET','POST'])
def index():
    data = {'Task':'Value'}
    if request.method == "POST":
        input = request.form['input1']
        if input:
            sql = f"SELECT TOP {input} place,mag FROM data6 ORDER BY mag DESC"
            c1.execute(sql)
            result = c1.fetchall()
            for Place, Mag in result:
                data[Place] = float(Mag)
        elif request.form.get('from') and request.form.get('to'):
            from_mag = float(request.form['from'])
            to_mag = float(request.form['to'])
            start = from_mag
            while(start <= to_mag):
                sql = "SELECT COUNT(*) AS COUNT FROM data6 WHERE MAG BETWEEN " + str(start) + " AND " + str(start + 1)
                c1.execute(sql)
                result = c1.fetchall()
                data[start] = result[0][0]
                start = start + 1
                print(data)
    return header_html+render_template("index.html",data=data)

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)