import numpy as np
import pandas as pd
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

df = pd.read_csv('covid_19_data.csv')

df = df.rename(columns = {'Country/Region':'Country'})
df= df.rename(columns = {"ObservationDate":'Date'})

df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending = False)

df_countries = df_countries.drop_duplicates(subset = ['Country'])

df_countries = df_countries[df_countries['Confirmed'] > 0]

fig = go.Figure(data = go.Choropleth(locations = df_countries['Country'], 
                                     locationmode = 'country names',
                                     z = df_countries['Confirmed'],
                                     colorscale = 'Reds',
                                     marker_line_color = 'black',
                                     marker_line_width = 0.5))

fig.update_layout(title_text = 'Confirmed Cases as of March 28 2020', 
           title_x = 0.5,
           geo = dict(showframe = False, showcoastlines = False,
                      projection_type = 'equirectangular'))

fig.show()