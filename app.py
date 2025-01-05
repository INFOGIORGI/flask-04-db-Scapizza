from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']="138.41.20.102"
app.config['MYSQL_PORT']=53306
app.config['MYSQL_USER']="ospite"
app.config['MYSQL_PASSWORD']="ospite"
app.config['MYSQL_DB']="w3schools"
mysql= MySQL(app)

@app.route("/")
def home():
    return render_template("index.html", titolo="Home")

@app.route("/products")
def products():
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    prodotti=cursor.fetchall()
    return render_template("products.html", titolo="prodotti", products=prodotti)

@app.route("/productsPerCat/<int:category>")
def productsPerCat(category):
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    prodotti=cursor.fetchall()
    selezionati=[]
    for p in prodotti:
        if(p[3]==category):
            selezionati.append(p)
    return render_template("productsPerCat.html", titolo="prodottiPerCat", prodotti=selezionati)

app.run(debug=True)



