from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

'''
# Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3306,
  database="dpace"
)

mycursor = mydb.cursor()
'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dpace'

mysql = MySQL(app)
# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM foods;')
    results = cursor.fetchall()
    #print ("Count is " + str(results))
    return render_template('index.html', results=results)

@app.route('/cart/<id>')
def cart(id):
     # Set The upload HTML template '\templates\index.html'
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM foods where id='+id+';')
    results = cursor.fetchall()
    #print ("Count is " + str(results))
    return render_template('cart.html', results=results)

#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        classification = request.form['classification']
        cursor.execute("SELECT * from foods where classify = '"+str(classification)+"'")
        results = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(results) == 0 and classification == 'all':
            cursor.execute("SELECT * from foods")
            results = cursor.fetchall()
        return render_template('search.html', results=results)
    return render_template('search.html')

@app.route('/detail/<id>', methods=['GET', 'POST'])
def update(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from foods where id = '"+id+"'")
    results1 = cursor.fetchall()
    cursor.execute("SELECT * from user_review where food_id = '"+id+"'")
    results2 = cursor.fetchall()
    if request.method == "POST":
        user_name = request.form["user_name"]
        comment = request.form['comment']
        cursor.execute("INSERT INTO user_review (user_name, food_id, comment) Values (%s, %s, %s)", (user_name, id, comment))
        mysql.connection.commit()
        cursor.execute("SELECT * from user_review where food_id = '"+id+"'")
        results2 = cursor.fetchall()
        cursor.close()
        return render_template('detail.html', results1=results1, results2=results2)
    cursor.close()
    return render_template('detail.html', results1=results1, results2=results2)
'''
@app.route('/detail/<id>')
def edit(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM foods where id='+id+';')
    results = cursor.fetchall()
    #print ("edit is " + str(results))
    return render_template('detail.html', results=results)

    '''
if (__name__ == "__main__"):
     app.run()
