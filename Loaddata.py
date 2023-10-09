# We import pandas into Python
import pandas as pd



# We load the Google stock data into a DataFrame
google_stock = pd.read_csv('C:/Users/user/Documents/UDACITY/UDACITY_PYTHON_PROJECT/docs/GOOG.csv')

# We load the Apple stock data into a DataFrame
apple_stock = pd.read_csv('C:/Users/user/Documents/UDACITY/UDACITY_PYTHON_PROJECT/docs/AAPL.csv')

# We load the Amazon stock data into a DataFrame
amazon_stock = pd.read_csv('C:/Users/user/Documents/UDACITY/UDACITY_PYTHON_PROJECT/docs/AMZN.csv')
# We display the google_stock DataFrame
print(google_stock.head())
print("/n New Set/n")
google_stoc = google_stock.rename(columns={'Adj Close':'Google'})
print(google_stoc.head())