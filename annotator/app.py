# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from .configure import AppConfigure
from .layout import MAIN, TITLE, CONTENT, ConfigLayout, MainLayout

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.layout = MAIN

appConfigure = AppConfigure()

# Set initial to config
CONTENT[:] = [TITLE, ConfigLayout, MainLayout]
