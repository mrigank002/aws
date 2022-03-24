from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

#Adding some comments random comments
app.config['MYSQL_HOST'] = 'database-1.c1xgaop7mcps.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'employee'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        experience= details['exp']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee_details(firstName, lastName, experience) VALUES (%s, %s)", (firstName, lastName,experience))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
