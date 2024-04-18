from flask import Flask, render_template, request
from waitress import serve
import requests_html
import lxml.html.clean
import pandas as pd
import numpy as np


app = Flask(__name__)
recommendations=[]
@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/About')
def About():
    return render_template("About.html")

@app.route('/Faqs')
def Faqs():
    return render_template("faq.html")

@app.route('/Howitworks')
def Howitworks():
   return render_template("Howitworks.html")


@app.route('/Risk')
def risk_profile():
    return render_template("Risk.html")

if __name__ == '__main__' :
    serve(app, host="0.0.0.0",port=8000)
