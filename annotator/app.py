# -*- coding: utf-8 -*-
import dash
from .configure import AppConfigure

app = dash.Dash(__name__)
app.title = "annotator"
app.config.suppress_callback_exceptions = True
appConfigure = AppConfigure()
