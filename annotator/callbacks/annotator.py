from dash.dependencies import Input, Output, State
import dash_html_components as html
from ..layout import ConfigLayout, MainLayout, TITLE, ClassUploadStyle, FolderSelectStyle, ClassUploadChildren
from ..utils import load_image
from ..app import app, appConfigure


@app.callback([Output('table', 'style_data_conditional'),
               Output('preview', 'src')],
              [Input('next', 'n_clicks'),
               Input('prev', 'n_clicks'),
               Input('table', 'derived_viewport_row_ids')])
def update_next(next, prev, page):
    if page != appConfigure._current_page:
        appConfigure._selected = 0
        appConfigure._current_page = page
    if next and next > appConfigure._next_clicks:
        appConfigure._next_clicks = next
        appConfigure._selected += 1
    if prev and prev > appConfigure._prev_clicks:
        appConfigure._prev_clicks = prev
        appConfigure._selected = max(appConfigure._selected-1, 0)
    return [{'if': {'row_index': 'odd'},
             'backgroundColor': 'rgb(248, 248, 248)'},
            {'if': {'row_index': appConfigure._selected},
             'backgroundColor': 'rgb(255, 0, 0)'}], load_image(appConfigure.files()[(appConfigure._current_page or [0])[appConfigure._selected or 0]]['path']) if appConfigure.files() else ''
