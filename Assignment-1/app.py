from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath

import pandas as pd
import mysql.connector

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


# Database
mydb = mysql.connector.connect(
  host="localhost",
  user="?",
  password="?",
  database="assignment1db"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

# View All Database
for x in mycursor:
  print(x)





# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM people;')
    #cursor.execute('SELECT picture FROM people where `name` like '+ param +';')
    results = cursor.fetchall()
    print ("Count is " + str(results))
    return render_template('index.html', people=results)

@app.route('/people/edit/<id>')
def edit(id):
     # Set The upload HTML template '\templates\index.html'
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM people where id='+id+';')
    #cursor.execute('SELECT picture FROM people where `name` like '+ param +';')
    results = cursor.fetchall()
    print ("edit is " + str(results))
    return render_template('edit.html', results=results)

@app.route('/people/update/<id>', methods=['POST'])
def update(id):
    salary = request.form.get('salary')
    keywords = request.form.get('keywords')
    cursor = mydb.cursor()
    cursor.execute('update people SET salary = '+salary+',keywords ="'+keywords+'" where id='+id+';')
    mydb.commit()
    results = cursor.fetchall()
    print ("Count is " + str(results))
    return redirect('/')
    return render_template('index.html', people=results)
# Get the uploaded files

@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV(file_path)
          # save the file
      return redirect(url_for('index'))

def parseCSV(filePath):
      # CVS Column Names
      col_names = ['name','salary','room', 'telnum', 'picture' , 'keywords']
      # Use Pandas to parse the CSV file

      csvData = pd.read_csv(filePath,names=col_names, header=None)
      csvData = csvData.where((pd.notnull(csvData)), None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
             sql = "INSERT INTO people (name, salary, room, telnum, picture, keywords) VALUES (%s, %s, %s, %s, %s, %s)"
             value = (row['name'],row['salary'],row['room'],row['telnum'],row['picture'],str(row['keywords']))
             mycursor.execute(sql, value)
             mydb.commit()
             print(i,row['name'],row['salary'],row['room'],row['telnum'],row['picture'],row['keywords'])

@app.route('/search' ,methods=['POST'])
def search() :
    cursor = mydb.cursor()
    param = request.form.get('query')
    print(request.form.get('query'))
    cursor.execute('SELECT * FROM people where name like \'%'+param+'%\';')
    results = cursor.fetchall()
    print ("Count is " + str(results))
    return render_template('searchpicture.html', results=results)

@app.route('/searchBySalary' ,methods=['POST'])
def searchPictureBySalary() :
    cursor = mydb.cursor()
    param = request.form.get('query')
    print(request.form.get('query'))
    cursor.execute('SELECT * FROM people where salary > \'%'+param+'%\';')
    results = cursor.fetchall()
    print ("Count is " + str(results))
    return render_template('searchBySalary.html', salaryResults=results)

if (__name__ == "__main__"):
     app.run(port = 5000)
