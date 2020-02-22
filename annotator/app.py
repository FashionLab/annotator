# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from .configure import AppConfigure

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
appConfigure = AppConfigure()
