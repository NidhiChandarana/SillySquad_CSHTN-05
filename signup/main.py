from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Arp123@'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'chatbot'
mysql = MySQL(app)


@app.route('/')
def main_page():
    return render_template("bank_web.html")


@app.route('/second')
def about():
    return render_template("about.html")

@app.route('/loginReg', methods=['GET', 'POST'])
def loginReg():
    return render_template("sign.html")
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['user_name']  # s_name in html file
        password = userDetails['password']
        name = userDetails['user_name']  # s_name in html file
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute( "SELECT * FROM login WHERE username LIKE %s and password LIKE %s", [name,password] )
        data = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        if(data != None):
            return render_template("bank_web.html")
        else:
            print("failed")
            return render_template("sign.html")


@app.route('/Reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['user_name']  # s_name in html file
        email = userDetails['email']
        password = userDetails['password']
        contact = userDetails['contact']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login(username,email,contact_no,password) VALUES(%s, %s,%s,%s)", (name, email, contact,password))
        mysql.connection.commit()
        cur.close()
        return render_template("sign.html")


app.run(debug=True)
