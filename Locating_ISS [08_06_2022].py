# Disclaimer, this is not real time tracker. But you can use this to track the location of the ISS during a specific time
# Import necessary packages
import pandas as pd # For loading the dataframe
import plotly.express as px # For plotting purposes

# The API that gives the longitue and latitude coordinates of the ISS
url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url) # The file type comes back as json format

# The dataframe will display information like latitude and longitude. It also includes the timestamp, which we will not be using
df['latitude'] = df.loc['latitude','iss_position'] # This creates a new column and sets the value of the latitude from the table
df['longitude'] = df.loc['longitude','iss_position'] # This creates a new column and sets the value of the longitude from the table
df.reset_index(inplace=True) # Creates new index

df = df.drop(['index','message'], axis=1) # Removes the old index column and the message column because we don't really want them

fig = px.scatter_geo(df, lat='latitude', lon='longitude') # From the df, we select the latitude and longitude to plot

print(fig.show()) # To display the figure
