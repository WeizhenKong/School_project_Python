#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:14:32 2019

@author: kongweizhen
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


df = pd.read_excel('https://s3.amazonaws.com/programmingforanalytics/NBA_data.xlsx')

app = dash.Dash(__name__)

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

options = numerical_features = ['James Harden','Paul George','Giannis Antetokounmpo','Joel Embiid','LeBron James','Stephen Curry','Kawhi Leonard','Devin Booker','Kevin Durant','Anthony Davis','Damian Lillard','Kemba Walker','Bradley Beal','Blake Griffin','Karl-Anthony Towns','Kyrie Irving','Donovan Mitchell','Zach LaVine','Russell Westbrook','Klay Thompson']
app.layout = html.Div(
    [
        html.Label(["Player 1", dcc.Dropdown(id="my-dynamic-dropdown")]),
        html.Label(
            ["Player 2", dcc.Dropdown(id="my-multi-dynamic-dropdown", multi=True),
            ]
        ),
    ]
)
        
@app.callback(
    dash.dependencies.Output("my-multi-dynamic-dropdown", "options"),
    [dash.dependencies.Input("my-multi-dynamic-dropdown", "search_value")],
    [dash.dependencies.State("my-multi-dynamic-dropdown", "value")],
)
def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    return [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]


if __name__ == "__main__":
    app.run_server(debug=True)