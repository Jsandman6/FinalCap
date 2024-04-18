from flask import Flask, render_template, request
from waitress import serve
import requests_html
import lxml.html.clean
import pandas as pd
import numpy as np
from Advisor import get_user_input, recommend_portfolio
from Assessment import risk_assessment_questionnaire

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
    age, income, risk_tolerance = get_user_input()
    recommended_portfolio = recommend_portfolio(age, income, risk_tolerance)
   return render_template("Howitworks.html", recommended_portfolio = recommended_portfolio)


@app.route('/Risk')
def risk_profile():
    return render_template("Risk.html")

if __name__ == '__main__' :
    serve(app, host="0.0.0.0",port=8000)
