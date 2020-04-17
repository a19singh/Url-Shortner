#!/usr/bin/pyhthon36

from flask import Flask, render_template ,request , redirect

import mysql.connector

import string
base= string.digits + string.ascii_letters
dictionary = dict((c,v) for v,c in enumerate (base))

from math import floor

def base62(sno):
    q = sno
    b=62
    res=""
    while q:
        r = q % b
        res = res +base[r]
        q = floor(q/b)
    return res

def base10(url):

    length = len(url)
    res=0
    b=62
    for i in range(length):
        res = b*res + dictionary[url[i]]
    return str(res)

def dbTable():

    mydb = mysql.connector.connect(
            host = "172.17.0.2",
            user = "root" ,
            password = "redhat",
            database = "mydatabase"
            )
    mycursor = mydb.cursor()
    try:
        mycursor.execute("""
            CREATE TABLE shorturl(
            ID INT PRIMARY KEY AUTO_INCREMENT,
            URL TEXT NOT NULL
            );
            """)
    except mysql.connector.Error:
        pass


app = Flask( __name__ )

@app.route('/', methods = ['POST' ,'GET'])
def longurl():

    if request.method == 'POST':
        url = request.form.get('url')
        mydb = mysql.connector.connect(
            host = "172.17.0.2",
            user = "root",
            password = "redhat",
            database = "mydatabase"
            )  
        mycursor = mydb.cursor()
        data = """
                INSERT INTO shorturl (URL)
                VALUES (\'%s\') """ %url
        mycursor.execute(data)
        short = base62(mycursor.lastrowid)
        mydb.commit()
        shortUrl= "http://localhost:5000/" + short
        return shortUrl
    return render_template('Short.html')



@app.route('/<url>')
def short_url(url):
    sno = str(base10(url))
    originalurl = 'http://localhost:5000'
    mydb = mysql.connector.connect(
            host = "172.17.0.2",
            user = "root",
            password = "redhat",
            database = "mydatabase"
            )
    mycursor = mydb.cursor()
    extract = """
            SELECT URL FROM shorturl
            WHERE ID=%s """ %(sno)
    mycursor.execute(extract)
    try :
        originalurl = mycursor.fetchone()[0]
    except Exception as e:
        print(e)
    return originalurl

if __name__ == '__main__':

    dbTable()
    app.run(host="0.0.0.0", debug=True)



        



