from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table, get_analysts_info
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests_html


def get_user_input():
  age = int(input("Enter your age: "))
  income = float(input("Enter your annual income: "))
  risk_tolerance = input("Enter your risk tolerance (low, medium, high): ")
  return age, income, risk_tolerance

# Define a function to recommend a portfolio
def recommend_portfolio(age, income, risk_tolerance):
  # Create a DataFrame of investment options
  options = pd.DataFrame({
    "Asset Class": ["Stocks", "Bonds", "Real Estate", "Commodities"],
    "Risk Level": ["High", "Low", "Medium", "High"],
    "Expected Return": [7.0, 3.0, 5.0, 10.0]
  })

  # Filter options based on risk tolerance
  if risk_tolerance == "low":
    options = options[options["Risk Level"] == "Low"]
  elif risk_tolerance == "medium":
    options = options[(options["Risk Level"] == "Low") | (options["Risk Level"] == "Medium")]
  elif risk_tolerance == "high":
    options = options

  # Calculate the recommended allocation based on age and income
  allocation = np.array([0.7, 0.2, 0.1, 0.0])
  if age < 30:
    allocation[0] += 0.1
    allocation[1] -= 0.1
  elif age > 50:
    allocation[0] -= 0.1
    allocation[1] += 0.1

  if income < 50000:
    allocation[2] += 0.1
    allocation[3] -= 0.1
  elif income > 100000:
    allocation[2] -= 0.1
    allocation[3] += 0.1

  # Recommend the portfolio
  recommended_portfolio = pd.DataFrame({
    "Asset Class": options["Asset Class"],
    "Allocation": allocation * 100
  })

  return recommended_portfolio


# Get user input
age, income, risk_tolerance = get_user_input()

# Recommend a portfolio
recommended_portfolio = recommend_portfolio(age, income, risk_tolerance)

if __name__ == '__main__' :
 print("Recommended Portfolio:")
 print(recommended_portfolio.to_string())