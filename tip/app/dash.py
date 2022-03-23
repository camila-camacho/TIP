import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json


from urllib import response
from urllib.request import urlopen
from flask_login.utils import login_required

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


url = "https://g43bee37532bd29-dblab1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/"
response = urlopen(url)
monthly_raised = json.loads(response.read())['items']

months=[]
data=[]

for element in monthly_raised:
    months.append(element["month"])
    data.append(element["incidences_number"])

df = pd.DataFrame({'Months': months, 'Data': data})



def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/raised/")
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Raised Dashboard"),
            html.Div(
                children="""
                                   Number of Incidences per Month 
        """
            ),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df, x="Months", y="Data"),
            ),
        ]
    )


    return dash_app
