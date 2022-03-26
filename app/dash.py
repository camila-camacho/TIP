import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json
import requests


from urllib import response
from urllib.request import urlopen
from flask_login.utils import login_required
import pandas as pd 
import numpy as np
from dash import Dash, dash_table

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

def kpi2_solve_month_r():
    url = 'https://g43bee37532bd29-dblab1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi2/incsolved/'
    data_oracle = requests.get(url).json()['items']
    data_oracle= pd.DataFrame(data_oracle)
    return data_oracle

def kpi3_solve_monthprior_r():
    url = 'https://g43bee37532bd29-dblab1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi3/raisedpriority/'
    data_oracle = requests.get(url).json()['items']
    data_oracle= pd.DataFrame(data_oracle)
    critical = data_oracle[data_oracle['priority']=='Crítica']
    alta = data_oracle[data_oracle['priority']=='Alta']
    media = data_oracle[data_oracle['priority']=='Media']
    baja = data_oracle[data_oracle['priority']=='Baja']
    return critical, alta, media, baja

def kpi4_cause_incident_b(): #incident type and number 
    url = 'https://g43bee37532bd29-dblab1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi4/backcause'
    data_oracle = requests.get(url).json()['items']
    data_oracle= pd.DataFrame(data_oracle)
    return data_oracle

def kpi7_incident_b():
    url= 'https://g43bee37532bd29-dblab1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi7/incidentstatus/'
    data_oracle = requests.get(url).json()['items']
    data_oracle= pd.DataFrame(data_oracle)
    return data_oracle

def kpi8_cause_incident_c(): #incident type and number 
    url= 'https://g43bee37532bd29-dblab1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi8/cc/'
    data_oracle = requests.get(url).json()['items']
    data_oracle= pd.DataFrame(data_oracle)
    return data_oracle

def kpi9_priority_closed(): #number of incidences month and priority
    url= 'https://g43bee37532bd29-dblab1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi9/closeprio/'
    data_oracle = requests.get(url).json()['items']
    data_oracle= pd.DataFrame(data_oracle)
    critical = data_oracle[data_oracle['priority']=='Crítica']
    alta = data_oracle[data_oracle['priority']=='Alta']
    media = data_oracle[data_oracle['priority']=='Media']
    baja = data_oracle[data_oracle['priority']=='Baja']
    return critical, alta, media, baja



def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/raised/")
    
    df2= kpi2_solve_month_r()
    df3= kpi3_solve_monthprior_r()

    
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Raised Dashboard"),
            html.Div(html.H4("Number of Incidents per Month")),
            dcc.Graph(
                id="kpi2-graph",
                figure=px.bar(df2, x="month", y="incidences_number", barmode="group"),
            ),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df3[0]['month'], 'y': df3[0]['incidences_number'], 'type': 'bar', 'name': 'Critical'},
                        {'x': df3[1]['month'], 'y': df3[1]['incidences_number'], 'type': 'bar', 'name': 'Alto'},
                        {'x': df3[2]['month'], 'y': df3[2]['incidences_number'], 'type': 'bar', 'name': 'Medio'},
                        {'x': df3[3]['month'], 'y': df3[3]['incidences_number'], 'type': 'bar', 'name': 'Bajo'},
                    ],
                    'layout': {
                        'title': 'Incidents Solved by Priority'
                    }
                }
            )
        ]
    )
    

    
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/backlog/")
    df4= kpi4_cause_incident_b()
    df7= kpi7_incident_b()
    
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Backlog Dashboard"),
            html.Div(html.H4("Incidents Status")),
            dcc.Graph(
                id="kpi7-graph",
                figure=px.bar(df7, x="incident_status", y="incident_status_number", barmode="group"),
            ),
            
            
            html.Div(html.H4("Number of Incidents by Type")),
            dash_table.DataTable(
                id='kpi4',
                columns=[
                    {"name": i, "id": i, "deletable": True, "selectable": True} for i in df4.columns
                ],
                data=df4.to_dict('records'),
                editable=False,
                sort_action="native",
                sort_mode="multi",
                row_deletable=False,
                fixed_columns=True,
                selected_columns=[],
                selected_rows=[],
                page_current= 0,
                page_size= 15
            
            )
        ]
    )
    

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/close/")
    df8= kpi8_cause_incident_c()
    df9= kpi9_priority_closed()
    
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Closed Dashboard"),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df9[0]['month'], 'y': df9[0]['incidences_number'], 'type': 'bar', 'name': 'Critical'},
                        {'x': df9[1]['month'], 'y': df9[1]['incidences_number'], 'type': 'bar', 'name': 'Alto'},
                        {'x': df9[2]['month'], 'y': df9[2]['incidences_number'], 'type': 'bar', 'name': 'Medio'},
                        {'x': df9[3]['month'], 'y': df9[3]['incidences_number'], 'type': 'bar', 'name': 'Bajo'},
                    ],
                    'layout': {
                        'title': 'Incidents Solved by Priority'
                    }
                }
            ),
            
            
            html.Div(html.H4("Number of Incidents by Type")),
            dash_table.DataTable(
                id='kpi8',
                columns=[
                    {"name": i, "id": i, "deletable": True, "selectable": True} for i in df8.columns
                ],
                data=df4.to_dict('records'),
                editable=False,
                sort_action="native",
                sort_mode="multi",
                row_deletable=False,
                fixed_columns=True,
                selected_columns=[],
                selected_rows=[],
                page_current= 0,
                page_size= 15
            )
            
        ]
    )
    
    return dash_app    
        
    
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    