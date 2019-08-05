import os
from app import app
from flask import render_template, request, redirect

# from flask_pymongo import PyMongo

# name of database
# app.config['MONGO_DBNAME'] = 'database-name' 

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri' 

# mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database

    # insert new data

    # return a message to the user
    return ""
    
@app.route('/mission')
def mission():
    return render_template("mission.html")

@app.route('/team')
def team():
    return render_template("team.html")
    
@app.route('/prod1')
def prod1():
    return render_template("prod1.html")
    
@app.route('/prod2')
def prod2():
    return render_template("prod2.html")
    
@app.route('/prod3')
def prod3():
    return render_template("prod3.html")
    
@app.route('/prod4')
def prod4():
    return render_template("prod4.html")
    
@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")
    
@app.route('/cart2')
def cart2():
    return render_template("cart2.html")
    
@app.route('/cart0')
def cart0():
    return render_template("cart0.html")
    
@app.route('/cart3')
def cart3():
    return render_template("cart3.html")
    
@app.route('/cart4')
def cart4():
    return render_template("cart4.html")